import pytest
from newa_downloader import core

AVAILABLE_HEIGHTS = [10.0, 15.0, 20.0]

AVAILABLE_VARIABLES = ["TEST1", "TEST2", "TEST3"]


def test_valid_height():
    heights = [10.0, 20.0]
    core.validate_heights(heights, AVAILABLE_HEIGHTS)


def test_invalid_height():
    heights = [10.0, 30.0]
    with pytest.raises(core.HeightError):
        core.validate_heights(heights, AVAILABLE_HEIGHTS)


def test_valid_variable():
    variables = ["TEST1", "TEST2"]
    core.validate_variables(variables, AVAILABLE_VARIABLES)


def test_invalid_variable():
    variables = ["TEST4"]
    with pytest.raises(core.VariableError):
        core.validate_variables(variables, AVAILABLE_VARIABLES)

