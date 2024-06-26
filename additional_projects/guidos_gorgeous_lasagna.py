"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.

'''
importing the lasagna class
created 2 constants, EXPECTED_BAKE_TIME which is set to 40 minutes, and PREPARATION_TIME which is set to 2 minutes
'''

import lasagna
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    if elapsed_bake_time >= EXPECTED_BAKE_TIME:
        return 0
    else:
        return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time remaining.

    :param number_of_layers: int - the number of layers provided, preperation time already established.
    :return: int - remaining preperation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the amount of layers the lasagna has as
    an argument and returns how many minutes the lasagna still needs to be prepared for
    based on the `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven.
    :return: int -  total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has 
    already spent baking in the oven..

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time