#!/usr/bin/env python3

"""
** Allows you to temporarily concatenate several streams. **
------------------------------------------------------------
"""


import fractions
import math
import typing

import numpy as np
import torch

from movia.core.classes.filter import Filter
from movia.core.classes.frame_audio import FrameAudio
from movia.core.classes.frame_video import FrameVideo
from movia.core.classes.node import Node
from movia.core.classes.stream import Stream
from movia.core.classes.stream_audio import StreamAudio
from movia.core.classes.stream_video import StreamVideo
from movia.core.exceptions import OutOfTimeRange



class FilterChain(Filter):
    """
    ** Concatenate the streams end-to-end. **

    Examples
    --------
    >>> from movia.core.filters.basic.chain import FilterChain
    >>> from movia.core.filters.basic.truncate import FilterTruncate
    >>> from movia.core.generation.video.noise import GeneratorVideoNoise
    >>>
    >>> (s_video_0,) = FilterTruncate(GeneratorVideoNoise(0, (3, 3)).out_streams, 10).out_streams
    >>> (s_video_1,) = GeneratorVideoNoise(.5, (3, 3)).out_streams
    >>> (s_chain_video,) = FilterChain([s_video_0, s_video_1]).out_streams
    >>>
    >>> (s_video_0.snapshot(0) == s_chain_video.snapshot(0)).all()
    tensor(True)
    >>> (s_video_1.snapshot(0) == s_chain_video.snapshot(10)).all()
    tensor(True)
    >>> (s_video_1.snapshot(10) == s_chain_video.snapshot(20)).all()
    tensor(True)
    >>>
    """

    def __init__(self, in_streams: typing.Iterable[Stream]):
        """
        Parameters
        ----------
        in_streams : typing.Iterable[Stream]
            Forwarded to ``movia.core.classes.filter.Filter``.
            The streams are concatenated in the order provided.
            That is to say the stream of index 0 will appear first.
        """
        super().__init__(in_streams, in_streams)
        if not self.in_streams:
            return
        kind = {s.type for s in self.in_streams}
        assert len(kind) == 1, f"impossible to chain different type of streams {kind}"
        kind = kind.pop()
        assert kind != "audio", "not yet implemented"
        if kind == "audio":
            super().__init__(self.in_streams, [_StreamAudioChain(self)])
        elif kind == "video":
            super().__init__(self.in_streams, [_StreamVideoChain(self)])
        else:
            raise NotImplementedError(f"not yet supported {kind}")

    @classmethod
    def default(cls):
        return cls([])

    def getstate(self) -> dict:
        return {}

    def setstate(self, in_streams: typing.Iterable[Stream], state: dict) -> None:
        assert state == {}
        FilterChain.__init__(self, in_streams)


class _StreamAudioChain(StreamAudio):
    """
    ** Concatenate the audio streams. **
    """

    def __init__(self, node: Node):
        """
        Parameters
        ----------
        node : movia.core.filters.basic.chain.FilterChain
            The node containing the StreamAudio to chain.
        """
        assert isinstance(node, FilterChain), node.__class__.__name__
        assert node.in_streams, "requires at least 1 stream to chain"
        super().__init__(node)

    def _snapshot(self, timestamp: fractions.Fraction, rate: int, samples: int) -> FrameAudio:
        # retrive time information of each slices
        slice_start = timestamp
        slice_end = timestamp + fractions.Fraction(samples, rate)
        cum_duration = np.cumsum([s.duration for s in self.node.in_streams])
        abs_starts = np.concatenate([[self.beginning], self.beginning + cum_duration[:-1]])
        abs_ends = cum_duration + self.beginning

        # verification the slice requiere is in the good intervalle
        if slice_start < abs_starts[0] or slice_end >= abs_ends[-1]:
            raise OutOfTimeRange(
                f"stream start {abs_starts[0]} and end {abs_ends[-1]}, "
                f"start {slice_start} and end {slice_end} are requiered"
            )

        # selection of the streams witch overlap the slice
        streams = [
            (stream, max(slice_start, abs_start), min(slice_end, abs_end)) # stream, start, end
            for stream, abs_start, abs_end in zip(self.node.in_streams, abs_starts, abs_ends)
            if slice_end >= abs_start and slice_start < abs_end
        ]
        streams = [
            (stream, abs_end-abs_start, abs_start-stream_start) # stream, duration, shift
            for (stream, abs_start, abs_end), stream_start in zip(streams, abs_starts)
        ]
        print(streams)
        streams = [
            (stream, stream.beginning+shift, math.ceil(duration*rate)-1) # stream, relstart, samples
            for stream, duration, shift in streams
        ]
        print(streams)

        # extart each slices of samples
        slices = [
            stream._snapshot(start, rate, samples)
            for stream, start, samples in streams if samples > 0
        ]
        if len({s.shape[0] for s in slices}) != 1:
            raise NotImplementedError("impossible to mix different channels audio")

        # concatenate each slice
        return FrameAudio(
            timestamp, rate, torch.concatenate(slices, axis=1) if len(slices) >= 2 else slices.pop()
        )


    @property
    def beginning(self) -> fractions.Fraction:
        return self.node.in_streams[0].beginning

    @property
    def channels(self) -> int:
        if len(channels := {s.channels for s in self.node.in_streams}) != 1:
            raise AttributeError(f"chained streams do not have same channels {channels}")
        return channels.pop()

    @property
    def duration(self) -> typing.Union[fractions.Fraction, float]:
        return sum(s.duration for s in self.node.in_streams)

    @property
    def is_time_continuous(self) -> bool:
        val = None
        for stream in self.node.in_streams:
            if val is None:
                val = stream.is_time_continuous
            elif val != stream.is_time_continuous:
                raise AttributeError("chained streams are both time continuous and discrete")
        return val


class _StreamVideoChain(StreamVideo):
    """
    ** Concatenate the video streams. **
    """

    def __init__(self, node: Node):
        """
        Parameters
        ----------
        node : movia.core.filters.basic.chain.FilterChain
            The node containing the StreamVideo to chain.
        """
        assert isinstance(node, FilterChain), node.__class__.__name__
        assert node.in_streams, "requires at least 1 stream to chain"
        super().__init__(node)

    def _snapshot(self, timestamp: fractions.Fraction) -> FrameVideo:
        errors = []
        rel_timestamp = timestamp
        for i, stream in enumerate(self.node.in_streams):
            beginning = stream.beginning if i else 0
            try:
                frame = stream._snapshot(rel_timestamp + beginning)
            except OutOfTimeRange as err:
                rel_timestamp -= stream.duration
                errors.append(err)
            else: # change time
                return FrameVideo(timestamp, frame)
        raise OutOfTimeRange(*(arg for err in errors for arg in err.args))

    @property
    def beginning(self) -> fractions.Fraction:
        return self.node.in_streams[0].beginning

    @property
    def duration(self) -> typing.Union[fractions.Fraction, float]:
        return sum(s.duration for s in self.node.in_streams)

    @property
    def height(self) -> int:
        if len(height := {s.height for s in self.node.in_streams}) != 1:
            raise AttributeError(f"chained streams do not have same height {height}")
        return height.pop()

    @property
    def is_space_continuous(self) -> bool:
        val = None
        for stream in self.node.in_streams:
            if val is None:
                val = stream.is_space_continuous
            elif val != stream.is_space_continuous:
                raise AttributeError("chained streams are both space continuous and discrete")
        return val

    @property
    def is_time_continuous(self) -> bool:
        val = None
        for stream in self.node.in_streams:
            if val is None:
                val = stream.is_time_continuous
            elif val != stream.is_time_continuous:
                raise AttributeError("chained streams are both time continuous and discrete")
        return val

    @property
    def width(self) -> int:
        if len(width := {s.width for s in self.node.in_streams}) != 1:
            raise AttributeError(f"chained streams do not have same width {width}")
        return width.pop()
