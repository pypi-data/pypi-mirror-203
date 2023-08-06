#!/usr/bin/env python3

"""
** Allows you to temporarily limit a sequence. **
-------------------------------------------------
"""



import fractions
import math
import numbers
import typing

from movia.core.classes.filter import Filter
from movia.core.classes.frame_audio import FrameAudio
from movia.core.classes.frame_video import FrameVideo
from movia.core.classes.stream import Stream
from movia.core.classes.stream_audio import StreamAudioWrapper
from movia.core.classes.stream_video import StreamVideoWrapper
from movia.core.exceptions import OutOfTimeRange



class FilterTruncate(Filter):
    """
    ** Shortens the duration of a stream. **

    Attributes
    ----------
    duration_max : fractions.Fraction
        The maximum duration beyond which the flows do not return anything (readonly).

    Examples
    --------
    >>> import fractions
    >>> from movia.core.exceptions import OutOfTimeRange
    >>> from movia.core.filters.basic.truncate import FilterTruncate
    >>> from movia.core.generation.audio.noise import GeneratorAudioNoise
    >>> from movia.core.generation.video.noise import GeneratorVideoNoise
    >>>
    >>> (s_base_audio,) = GeneratorAudioNoise(0).out_streams
    >>> (s_base_video,) = GeneratorVideoNoise(0, (3, 3)).out_streams
    >>> s_trunc_audio, s_trunc_video = FilterTruncate([s_base_audio, s_base_video], 10).out_streams
    >>>
    >>> _ = s_base_audio.snapshot(10-fractions.Fraction(1, 1000), 1000, 1)
    >>> try:
    ...     s_trunc_audio.snapshot(10-fractions.Fraction(1, 1000), 1000, 1)
    ... except OutOfTimeRange as err:
    ...     print(err)
    ...
    the stream has been truncated over 10 seconds, evaluation at 9999/1000 + 1/1000 seconds
    >>>
    >>> _ = s_base_video.snapshot(10)
    >>> try:
    ...     s_trunc_video.snapshot(10)
    ... except OutOfTimeRange as err:
    ...     print(err)
    ...
    the stream has been truncated over 10 seconds, evaluation at 10 seconds
    >>>
    """

    def __init__(self, in_streams: typing.Iterable[Stream], duration_max: numbers.Real):
        """
        Parameters
        ----------
        in_streams : typing.Iterable[Stream]
            Forwarded to ``movia.core.classes.filter.Filter``.
        duration_max : numbers.Real
            The maximal duration of the new stream.
        """
        assert hasattr(in_streams, "__iter__"), in_streams.__class__.__name__
        in_streams = tuple(in_streams)
        assert all(isinstance(stream, Stream) for stream in in_streams), \
            [stream.__class__.__name__ for stream in in_streams]
        assert isinstance(duration_max, numbers.Real), duration_max.__class__.__name__
        assert duration_max >= 0, duration_max

        try:
            self._duration_max = fractions.Fraction(duration_max)
        except OverflowError:
            self._duration_max = math.inf
        super().__init__(in_streams, in_streams)
        super().__init__(
            self.in_streams, # not in_stream without self because generator can be exausted
            [
                (
                    {"audio": _StreamAudioTruncate, "video": _StreamVideoTruncate}
                )[in_stream.type](self, index) for index, in_stream in enumerate(self.in_streams)
            ]
        )

    @classmethod
    def default(cls):
        return cls([], math.inf)

    @property
    def duration_max(self) -> fractions.Fraction:
        """
        ** The maximum duration beyond which the flows do not return anything. **
        """
        return self._duration_max

    def getstate(self) -> dict:
        return {"duration_max": str(self.duration_max)}

    def setstate(self, in_streams: typing.Iterable[Stream], state: dict) -> None:
        assert set(state) == {"duration_max"}, set(state)-{"duration_max"}
        if state["duration_max"] == "inf":
            duration_max = math.inf
        else:
            duration_max = fractions.Fraction(state["duration_max"])
        FilterTruncate.__init__(self, in_streams, duration_max)


class _StreamAudioTruncate(StreamAudioWrapper):
    """
    ** Truncates the end of an audio stream after a certain time. **
    """

    def _snapshot(self, timestamp: fractions.Fraction, rate: int, samples: int) -> FrameAudio:
        # for optimisation, self.duration is not invocated,
        # if duration_max > duration, the OutTimeRange exception will be raises from child.
        if timestamp + fractions.Fraction(samples, rate) >= self.beginning + self.node.duration_max:
            raise OutOfTimeRange(
                "the stream has been truncated over "
                f"{self.beginning+self.node.duration_max} seconds, "
                f"evaluation at {timestamp} + {samples}/{rate} seconds"
            )
        return self.stream._snapshot(timestamp, rate, samples)

    @property
    def duration(self) -> typing.Union[fractions.Fraction, float]:
        return min(self.node.duration_max, self.stream.duration)


class _StreamVideoTruncate(StreamVideoWrapper):
    """
    ** Truncates the end of a video stream after a certain time. **
    """

    def _snapshot(self, timestamp: fractions.Fraction) -> FrameVideo:
        if timestamp >= self.beginning + self.duration:
            raise OutOfTimeRange(
                f"the stream has been truncated over {self.beginning+self.duration} seconds, "
                f"evaluation at {timestamp} seconds"
            )
        return self.stream._snapshot(timestamp)

    @property
    def duration(self) -> typing.Union[fractions.Fraction, float]:
        return min(self.node.duration_max, self.stream.duration)
