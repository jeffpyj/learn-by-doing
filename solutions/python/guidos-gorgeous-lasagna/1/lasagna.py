"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    if elapsed_bake_time < 0:
        return EXPECTED_BAKE_TIME

    if elapsed_bake_time > EXPECTED_BAKE_TIME:
        return 0

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes

    Parameters:
        number_of_layers (int): Number of lasagna layers

    Returns:
        int: The preparation time needed for lasagna

    Function that takes the number of layers of lasagna as an argument and returns
    how many minutes the it will take to prepare it based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total time elapsed in kitchen cooking

    Parameters:
        number_of_layers (int): Number of lasagna layers
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total time elapsed making the lasagna

    Function that takes the number of layers of lasagna and the actual
    minutes the lasagna has been in the oven returns as arguments and returns
    how many minutes the it has elapsed for making the lasagna
    """
    if number_of_layers < 1:
        return 0

    if elapsed_bake_time < 0:
        return preparation_time_in_minutes(number_of_layers=number_of_layers)
    return (
        preparation_time_in_minutes(number_of_layers=number_of_layers)
        + elapsed_bake_time
    )
