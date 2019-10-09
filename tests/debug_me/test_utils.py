import pytest
from os import path

from consts import ONE_DIGITS_LENGTH, TWO_DIGITS_LENGTH
from debug_me.utils import (
    generate_possible_passwords,
    load_common_passwords,
    get_all_possible_passwords,
)


@pytest.fixture
def tests_directory():
    return path.dirname(__file__)


@pytest.fixture
def passwords_file_path(tests_directory):
    return path.join(tests_directory, "common_passwords.txt")


@pytest.mark.parametrize(
    "length,expected", [(1, ONE_DIGITS_LENGTH), (2, TWO_DIGITS_LENGTH)]
)
def test_generate_possible_passwords_different_lengths(length, expected):
    assert list(generate_possible_passwords(length)) == expected


@pytest.mark.parametrize("length,expected,start,end", [(1, ONE_DIGITS_LENGTH, 0, 15)])
def test_generate_possible_passwords_with_invalid_ranges(length, expected, start, end):
    assert list(generate_possible_passwords(length, start, end)) == expected


@pytest.mark.parametrize(
    "length,expected,start,end",
    [(1, ONE_DIGITS_LENGTH[:5], 0, 5), (1, ONE_DIGITS_LENGTH[5:], 5, 10)],
)
def test_generate_possible_passwords_different_ranges(length, expected, start, end):
    assert list(generate_possible_passwords(length, start, end)) == expected


def test_load_common_passwords_happy_flow(passwords_file_path):
    passwords = list(load_common_passwords(passwords_file_path))

    assert len(passwords) == 100
    assert "123456" in passwords
    assert "ginger" in passwords
    assert "love" in passwords


def test_get_all_possible_passwords(passwords_file_path):
    passwords = list(get_all_possible_passwords(common_passwords_path=passwords_file_path))
    second_passwords = list(get_all_possible_passwords(common_passwords_path=passwords_file_path))
    assert passwords == second_passwords
