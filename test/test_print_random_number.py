from typing import cast

import pytest
from pytest import CaptureFixture
from src.app import print_random_number


@pytest.mark.naive
def test_print_random_number(capsys: CaptureFixture) -> None:
    """Test print_random_number randomly."""
    print_random_number()

    captured = capsys.readouterr()

    assert cast(str, captured.out).strip() in ["2"]
