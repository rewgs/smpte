from .framerate import Framerate
from .timecode import Timecode, subtract


class Cue:
    """ Defines a single piece of music. """
    def __init__(self, number: str, name: str, start: str|Timecode, end: str|Timecode):
        self._framerate: Framerate
        self.number: str = number
        self.name: str = name
        # TODO: Change Timecode to Drop or Nondrop
        # self.start: Timecode = start if isinstance(start, Timecode) else Timecode(self._framerate, start)
        # self.end: Timecode = end if isinstance(end, Timecode) else Timecode(self._framerate, end)

    # TODO: Timecode needs __eq__, etc to work.
    def get_duration(self) -> Timecode:
        """ Returns the duration of the cue as a Timecode object. """
        duration = subtract(self.end, self.start)
        return duration

    @property
    def framerate(self) -> Framerate:
        return self._framerate

    @framerate.setter
    def framerate(self, value: Framerate) -> None:
        self._framerate = value
