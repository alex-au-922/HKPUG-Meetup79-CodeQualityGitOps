import random
from typing import cast

import pytest
from pytest import CaptureFixture, MonkeyPatch
from src.app import print_random_number_smart


@pytest.mark.robust
@pytest.mark.parametrize(
    "random_func_output,expected_output",
    [
        pytest.param(
            i / 10, i + 1, id=f"random_output = {i / 10}, expected_output = {i + 1}"
        )
        for i in range(10)
    ],
)
def test_print_random_number_smart_robust(
    capsys: CaptureFixture,
    monkeypatch: MonkeyPatch,
    random_func_output: float,
    expected_output: int,
) -> None:
    """Test print_random_number_smart with random output set dynamically."""
    monkeypatch.setattr(random, "random", lambda: random_func_output)

    print_random_number_smart()

    captured = capsys.readouterr()

    assert cast(str, captured.out).strip() in [str(expected_output)]
    monkeypatch.undo()
