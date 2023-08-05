SAMPLERATE = 44100

import numpy as np
import sounddevice as sd
import soundfile as sf
from datetime import datetime

from .space import Space
from .tone import Tone


class Shape(object):
    """An object defined by x and y coordinates
    scaled to fit  the borders of space attribute.

    x and y are single-dimensional arrays

    Can contain an embedded object of the same type
    with implemented recursive access to the values

    methods defined here:
    to_device(): sends the values to sound device
    to_wav(): creates a wav-file with values
    switch(mode: {'fast', 'slow'}): switches the mode
    add(x: np.ndarray, y: np.ndarray): adds embedded object of the same type

    Note: When using Shape object in context of Jupyter notebook
    it is strongly recommended to pass its values directly to the
    IPython.display.Audio() method, which provides
    play/pause control,  so you can easily replay the sound
    without executing the code again.

    Example:

    from IPython.display import Audio
    sr = 1000
    f = 7
    samples = 1000
    x = np.arange(samples)
    y = np.sin(2 * np.pi * f * x / sr)
    sinusoid  = Shape(x, y)
    Audio(sinusoid.values, rate=44100)

    in any other cases you should use to_device() method instead
    and replace just the last line like this:

    sinusoid.to_device()

    Note: To create a histogram, you can use the  Shape object with proper x and y,
    but there is an option   to use an instance  of Histogram class,
    which inherits everything from Shape
    but its constructor takes  a distribution itself and a variaty of
    optional keyword arguments as well.

    Example:

    from scipy.stats import norm
    normal_distribution = norm.rvs(size=10000)
    histogram = Histogram(normal_distribution, bins=100, density=False, smooth=False, window_size=3, mode='fast')
    # and either
    Audio(histogram.values, rate=44100)
    # or just
    histogram.to_device()

    Note: Because any space is square-shaped,
    it can  produce some unexpected results when using embedded shapes -
    a line which is single and neither horizontal nor  vertical, is diagonal.

    """

    def __init__(self, x=np.array([0]), y=np.array([0]), mode="fast"):
        if len(x) != len(y):
            raise ValueError("Arguments x and y must be of the same length")
        self.space = Space()
        self.switch(mode)
        self.__x = x
        self.__y = y
        self.__values = None

    @property
    def x(self):
        return np.radians(self.space.x.bind(self.__x))

    @x.setter
    def x(self, values):
        self.__x = values

    @property
    def y(self):
        return self.space.y.bind(self.__y)

    @y.setter
    def y(self, values):
        self.__y = values

    @property
    def values(self):
        """Returns values shaped like (n_channels, n_samples)"""
        values = np.array([[], []])
        for x_value, y_value in zip(self.x, self.y):
            values = np.hstack(
                (
                    values,
                    Tone(
                        frequency=y_value,
                        duration=self.segment_duration,
                        deviation=x_value,
                    ).values,
                )
            )
        values = np.nan_to_num(values)
        if self.__values is not None:
            return np.hstack((values, self.__values.values))
        return values

    def switch(self, mode: {"fast", "slow"}) -> None:
        """Sets either 0.01 (fast mode) or 0.05 (slow mode)"""
        modes = {"fast": 0.01, "slow": 0.05}
        if mode not in modes.keys():
            raise ValueError(f"{mode} is not a valid value for the argument")
        self.segment_duration = modes[mode]

    def add(self, x, y):
        if self.__values == None:
            self.__values = Shape(x, y)
            self.__values.segment_duration = self.segment_duration
        else:
            self.__values.add(x, y)

    def to_device(self):
        sd.play(self.values.T, samplerate=SAMPLERATE, blocking=False)
        sd.wait()

    def to_wav(self):
        now = datetime.now()
        time_format = "%Y-%m-%d_%H-%M-%S"
        filename = f"{now:{time_format}}.wav"
        sf.write(filename, self.values.T, SAMPLERATE)
