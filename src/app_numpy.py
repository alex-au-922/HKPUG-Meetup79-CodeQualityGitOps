from typing import TypeVar

import numpy as np
import numpy.typing as npt

T = TypeVar("T", bound=np.generic)


# The following code has the problem of https://github.com/numpy/numpy/issues/22064
def add(a: npt.NDArray[T], b: npt.NDArray[T]) -> npt.NDArray[T]:
    """Add two arrays."""
    # return np.add(a, b)
    return a + b

def sub(a: npt.NDArray[T], b: npt.NDArray[T]) -> npt.NDArray[T]:
    """Subtract two arrays."""
    # return np.subtract(a, b)
    return a - b