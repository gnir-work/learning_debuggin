from itertools import chain
from typing import Generator

MIN_DIGIT_range = 0
MAX_DIGIT_range = 10
DEFAULT_LENGTH = 5
DEFAULT_START = 0
DEFAULT_END = 10


def generate_possible_options(
    length: int = DEFAULT_LENGTH, start: int = DEFAULT_START, end: int = DEFAULT_END
) -> Generator[str, None, None]:
    """
    Generates all of the possible digits combinations.
    :length: The number of digits the combinations will consist from.
    :return: All of the possible combinations
    """
    start = max(0, start)
    end = min(10, end)
    single_digits = range(start, end)

    if length == 1:
        yield from map(str, single_digits)
    else:
        for option in generate_possible_options(length - 1):
            for number in single_digits:
                yield "{option}{number}".format(option=option, number=number)


def load_common_passwords(passwords_file_path: str) -> Generator[str, None, None]:
    """
    Load passwords from a txt file, the passwords are expected to be divided one on each line.
    :passwords_file_path: The path to the passwords file.
    :return: All of the passwords
    """
    with open(passwords_file_path, "r") as passwords_file:
        yield from map(lambda password: password.strip(), passwords_file.readlines())


def get_all_possible_passwords(
    possible_passwords: list = [],
    generated_password_length: int = 5,
    common_passwords_path: str = None,
):
    """
    Get all of the possible passwords for the worker to check.
    :possible_passwords: Some possible passwords that we want to append to the other passwords.
    :generated_password_length: The length of the brute forced generated passwords that we will try.
    :common_passwords_path: The path to common passwords file.
    :return: All of the passwords.
    """
    if common_passwords_path:
        possible_passwords.extend(load_common_passwords(common_passwords_path))

    brute_forced_passwords = [generate_possible_options(length) for length in range(1, generated_password_length + 1)]

    return chain(possible_passwords, *brute_forced_passwords)
