import numpy as np


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Space(object):
    """A  space defined by its dimensions, the class implements singleton pattern
    - there can be only one Space object during  the  session,
    all parameters are read only and cannot be modified"""

    class Dimension:
        """An inner class stores  the range of possible  values and encapsulates a method for   rescaling input values into that range"""

        def __init__(self, limits):
            self.__limits = limits

        @property
        def limits(self):
            return self.__limits

        def bind(self, values):
            return self.__rescale(values, *self.limits)

        def __rescale(self, values: np.ndarray, min: int, max: int) -> np.ndarray:
            """Rescales the passed values into the  range between min and max."""
            values_max, values_min = np.max(values), np.min(values)
            # in case of a single value
            if values_max == values_min:
                if values_max > len(values):
                    values[:] = len(values)
                elif values_min < 0:
                    values[:] = 0
                values_min, values_max = 0, len(values)
            return (values - values_min) / (values_max - values_min) * (max - min) + min

    def __init__(
        self,
        x_limits=(-45, 45),  # degrees
        y_limits=(220, 7040),  # A of small and fifth octave
    ):
        self.__x = self.Dimension(x_limits)
        self.__y = self.Dimension(y_limits)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f"Space ({self.__x.limits} degrees, {self.__y.limits} Hz)"
