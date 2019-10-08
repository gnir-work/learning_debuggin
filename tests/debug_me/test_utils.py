import pytest

from consts import ONE_DIGITS_LENGTH, TWO_DIGITS_LENGTH
from debug_me.utils import generate_possible_options


@pytest.mark.parametrize(
    "length,expected", [(1, ONE_DIGITS_LENGTH), (2, TWO_DIGITS_LENGTH)]
)
def test_pasten(length, expected):
    assert list(generate_possible_options(length)) == expected
