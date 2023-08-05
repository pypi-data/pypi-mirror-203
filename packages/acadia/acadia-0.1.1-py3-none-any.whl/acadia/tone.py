import numpy as np

from .shape import SAMPLERATE


class Tone(object):
    """A stereo signal  of given frequency, duration and panning position"""

    def __init__(self, frequency, duration, deviation=0):
        self.frequency = frequency
        self.duration = duration
        self.deviation = deviation

    @property
    def values(self):
        return self.__pan(self.__tone())

    def __tone(self) -> np.ndarray:
        """Returns a sine wave of given frequency and duration"""
        t = np.linspace(0, self.duration, int(SAMPLERATE * self.duration), False)
        return np.sin(2 * np.pi * self.frequency * t)

    def __pan(self, values: np.ndarray) -> np.ndarray:
        """Multiplies values by amplitude and transforms mono signal
        into a set of two   channels with effect
        of audible horizontal deviation from the central point
        """

        left = (
            np.sqrt(2)
            / 2.0
            * (np.cos(self.deviation) - np.sin(self.deviation))
            * values
        )
        right = (
            np.sqrt(2)
            / 2.0
            * (np.cos(self.deviation) + np.sin(self.deviation))
            * values
        )
        return np.vstack((left, right))
