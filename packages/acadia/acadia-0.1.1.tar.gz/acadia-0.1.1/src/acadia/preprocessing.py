import numpy as np


def smoothen(values: np.ndarray, window_size: int = 3) -> np.ndarray:
    """Applies the simple moving averages algorythm with passed window size to the values
    starting with values[0] + window_size element.
    The first window_size elements are replaced by values' minimum.
    """

    shift = np.array([float(np.min(values))] * window_size)
    return np.hstack(
        (
            shift,
            np.array(
                [
                    np.sum(values[i : i + window_size]) / window_size
                    for i in range(len(values[:-window_size]))
                ]
            ),
        )
    )
