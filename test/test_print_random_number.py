from typing import cast
from src.app import print_random_number
from pytest import CaptureFixture
import pytest

@pytest.mark.naive
def test_print_random_number(capsys: CaptureFixture) -> None:
    """Test print_random_number randomly."""
    
    print_random_number()
    
    captured = capsys.readouterr()
    
    assert cast(str, captured.out).strip() in ["2"]
    