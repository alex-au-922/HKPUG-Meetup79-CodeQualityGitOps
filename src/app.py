from functools import wraps
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T", bound=Callable)


def timer(
    func: Callable[P, T],
) -> Callable[P, T]:  # mypy will check the type of the function
    """Print the runtime of the decorated function."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        import time

        start = time.time()
        result = func(1, 2)  #! Mypy understands modern Python features
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result

    return wrapper


@timer
def greeting_without_type(name) -> str:
    """Greet the user with the given name."""
    return "Hello " + name


@timer
def greeting_with_mypy_ignored(name: int) -> str:
    """Greet the user with the given name."""
    return "Hello " + name  # type: ignore


@timer
def greeting_normal(name: int) -> str:
    """Greet the user with the given name."""
    return "Hello " + name  #! Only this line will be checked by mypy
