import numpy as np

from .shape import Shape
from .preprocessing import smoothen


def arg_manager(class_):
    def set_params(*args, **kwargs):
        defaults = dict(
            {
                "bins": 100,
                "density": False,
                "smooth": False,
                "window_size": 3,
                "mode": "fast",
            }
        )
        for arg in defaults.keys():
            if arg in kwargs.keys():
                defaults[arg] = kwargs[arg]
        return class_(*args, **defaults)

    return set_params


@arg_manager
class Histogram(Shape):
    """A decorated constructor function takes and then safely routes
    any set of optional parameters from  default dictionary,
    including some parameters of numpy.histogram(),
    smoothen() and constructor of the parent class itself:
    bins: int,  number of bins in histogram, default is 100,
    density: bool, see the density parameter of numpy.histogram()
        default is False,
    smooth: bool,  whether to apply simple moving averages algorythm
        to the values or not, default is False,
    window_size: int, window size for sma, makes sence only if smooth=True.
    mode: {'fast', 'slow'}, corresponds to the length of segment
        of the Shape in seconds, 0.01 and 0.05 accordingly
    """

    def __init__(self, values, **kwargs):
        if kwargs is None:
            raise ValueError("Default settings not found")
        bins, density, smooth, window_size, mode = kwargs.values()
        x = np.arange(bins)
        y = np.histogram(values, bins, density=density)[0]
        if smooth:
            y = smoothen(y, window_size)
        super().__init__(x, y, mode)
