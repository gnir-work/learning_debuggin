from typing import Generator


def generate_possible_options(length: int = 5) -> Generator:
    """
    Generates all of the possible digits combinations.
    :length: The number of digits the combinations will consist from.
    :return: All of the possible combinations
    """
    if length == 1:
        yield from map(str, range(10))
    else:
        for option in generate_possible_options(length - 1):
            for number in range(10):
                yield "{option}{number}".format(option=option, number=number)
