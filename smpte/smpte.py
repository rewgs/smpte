from dataclasses import dataclass
from enum import Enum


class Framerate(Enum):
    FILM = 24
    TV = 29.97
    VIDEO = 30
    GAME = 60


class Timecode:
    def __init__(self, fr: Framerate, tc: str):
        self.__split: list[str] = self.__split_timecode(tc)
        self.hours: int = int(self.__split[0])
        self.minutes: int = int(self.__split[1])
        self.seconds: int = int(self.__split[2])
        self.__fr: dict[str,int] = self.__validate_framerate(fr, int(self.__split[3]))
        # self.framerate: int = self.__fr["framerate"]
        # self.frames: int = self.__fr["frames"]

    @staticmethod
    def __split_timecode(tc: str) -> list[str]:
        try:
            split: list[str] = tc.split(":", 4)
        # TODO: Actually handle this error, specify what to do with different Exceptions, etc.
        except Exception as error:
            raise error
        else:
            return split

    @staticmethod
    def __validate_framerate(fr: Framerate, frames: int) -> dict[str,int]:
        """
        Returns a framerate (int) and number of frames (int).
        """

        return {
            # NOTE: Temp values
            "framerate": 1,
            "frames": 1,
        }



class TimecodeCalculator:
    def __init__(self, framerate: Framerate, start: str, end: str):
        self.framerate: Framerate = framerate
        self.start: Timecode = Timecode(self.framerate, start)
        self.end: Timecode = Timecode(self.framerate, end)

    def calculate(self):
        ...



