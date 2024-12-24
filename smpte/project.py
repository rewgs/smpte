from .cue import Cue
from .framerate import Framerate
from .timecode import Timecode


class Project:
    """ Defines a scoring project -- a film, TV show, etc. """
    def __init__(self, name: str, code: str, framerate: Framerate):
        self.name: str = name
        self.code: str = code
        self.framerate: Framerate = framerate
        self.cues: list[Cue]

    def register_cue(self, cue: Cue):
        if cue not in self.cues:
            self.cues.append(cue)
            cue.framerate = self.framerate

    def get_time_between(a: Cue, b: Cue) -> Timecode:
        """ Returns the time between cues a and b as a Timecode object. """
