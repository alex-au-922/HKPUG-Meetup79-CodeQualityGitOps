import random
from contextlib import contextmanager, nullcontext
from typing import Generator, Optional


@contextmanager
def random_seed(seed: int) -> Generator[None, None, None]:
    """Sets the random seed for the duration of the context."""
    curr_seed = random.getstate()
    try:
        random.seed(seed)
        yield
    finally:
        random.setstate(curr_seed)


def print_random_number(seed: Optional[int] = None) -> None:
    """Prints a random number between 1 and 10."""
    context_manager = random_seed(seed) if seed is not None else nullcontext()

    with context_manager:
        num = random.random()

        if 0 <= num < 0.1:
            print("1")
        elif 0.1 <= num < 0.2:
            print("2")
        elif 0.2 <= num < 0.3:
            print("3")
        elif 0.3 <= num < 0.4:
            print("4")
        elif 0.4 <= num < 0.5:
            print("5")
        elif 0.5 <= num < 0.6:
            print("6")
        elif 0.6 <= num < 0.7:
            print("7")
        elif 0.7 <= num < 0.8:
            print("8")
        elif 0.8 <= num < 0.9:
            print("9")
        elif 0.9 <= num < 1:
            print("10")
