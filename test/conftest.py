from typing import Generator
from pytest import MonkeyPatch
import pytest
import random

@pytest.fixture
def set_random_output_0_2(monkeypatch: MonkeyPatch) -> Generator[None, None, None]:
    """Sets the random output to 0.2."""
    try:
        monkeypatch.setattr(random, "random", lambda: 0.2)
        yield
    finally:
        monkeypatch.undo()
