from typing import cast
from src.app import print_random_number
from pytest import CaptureFixture
import pytest

@pytest.mark.smart
@pytest.mark.usefixtures('set_random_output_0_2')
def test_print_random_number_smart(capsys: CaptureFixture) -> None:
    """Test print_random_number with random output set to 0.2."""
    
    print_random_number()
    
    captured = capsys.readouterr()
    
    assert cast(str, captured.out).strip() in ["3"]
