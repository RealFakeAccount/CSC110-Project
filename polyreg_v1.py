"""CSC110 Fall 2020 Course Project - Prototype version of polynomial regression algorithm.


Created by Arkaprava Choudhury,
in partnership with Ching Chang, Letian Cheng, and Hanrui Fan.

This file may be used freely by members of the team, as per their wish,
and by course instructors and teaching assistants when grading the project.
"""
from typing import List, Tuple
import numpy as np
import math
import matplotlib.pyplot as plt
import random

##############################################################
# Version 1
##############################################################


def poly_reg_v1() -> List[int]:
    """
    nnn
    """
    ...


def candidate_polynomial(points: List[Tuple[float, float]], degree: int) -> List[float]:
    """ A first try at getting the right 'shape' of the polynomial.

    Returns the polynomial generated by linear regression.

    """
    a_0, a_1 = simple_linear_regression(points)
    coefficients = [a_0, a_1]
    for i in range(degree - 2):
        coefficients.append(0)


def convert_points(points: List[Tuple[float, float]]) -> Tuple[List[float], List[float]]:
    """Return a tuple of two lists, containing the x- and y-coordinates of the given points.

    You may ASSUME that:
        - points is a list of tuples, where each tuple is a list of floats.

    >>> result = convert_points([(0.0, 1.1), (2.2, 3.3), (4.4, 5.5)])
    >>> result[0]  # The x-coordinates
    [0.0, 2.2, 4.4]
    >>> result[1]  # The y-coordinates
    [1.1, 3.3, 5.5]
    """
    return ([x[0] for x in points], [y[1] for y in points])


def simple_linear_regression(points: List[Tuple[float, float]]) -> Tuple[float, float]:
    """Perform a linear regression on the given points.

    points is a list of pairs of floats: [(x_1, y_1), (x_2, y_2), ...]
    This function returns a pair of floats (a, b) such that the line
    y = a + bx is the approximation of this data.

    Further reading: https://en.wikipedia.org/wiki/Simple_linear_regression

    You may ASSUME that:
        - len(points) > 0
        - each element of points is a tuple of two floats

    >>> simple_linear_regression([(1.0, 1.0), (2.0, 2.0), (3.0, 3.0)])
    (0.0, 1.0)

    Hint: you might want to define a separate function that calculates the average
    of a collection of numbers.
    """
    # Convert list of points into better format.
    list_of_points = convert_points(points)

    # Function to calculate mean values
    def mean_value(input_tuple: tuple, index: int) -> float:
        """ Return the mean value of the list at the specified index in input_tuple

        You may ASSUME that:
        - input_tuple is a tuple with two lists, both with the same length
        - index is a valid index for both lists
        - each element of the lists in input_tuple is a floats

        >>> mean_value(([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]), 0)
        2.0
        """
        return sum(input_tuple[index]) / len(input_tuple[index])

        # Calculate mean values.

    mean_x = mean_value(list_of_points, 0)
    mean_y = mean_value(list_of_points, 1)

    diff_x = [x - mean_x for x in list_of_points[0]]
    diff_y = [y - mean_y for y in list_of_points[1]]

    # Calculate b.
    numerator_b = sum([diff_x[i] * diff_y[i] for i in range(len(points))])
    denominator_b = sum(diff_x[i] ** 2 for i in range(len(points)))
    b = numerator_b / denominator_b

    # Calculate a.
    a = mean_y - (b * mean_x)

    # Return Simple Linear Regression model
    return (a, b)


def transform_to_coords(x_list: List[int], y_list: List[float]) -> List[Tuple[int, float]]:
    """Transform two lists of independent and dependent variable respectively,
    into a list of 2-tuples representing the coordinates.

    Preconditions:
      - len(x_list) == len(y_list)
      - x_list != []

    >>> transform_to_coords([1, 2], [1.0, 2.0])
    [(1, 1.0), (2, 2.0)]
    """
    list_of_coords = []
    for i in range(len(x_list)):
        point = (x_list[i], y_list[i])
        list_of_coords.append(point)
    return list_of_coords


class Polynomial:
    """Test case 1. Protype version 1.1.

    Defining polynomial function class to allow callables.

    Public Instance Attributes:
      - coefficients: the coefficients of the terms of the polynomial, from
                      highest order to lowest.
    """
    coefficients: List[float]

    def __init__(self, *coefficients) -> None:
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = list(coefficients)  # tuple is turned into a list

    def __repr__(self) -> str:
        """
        method to return the canonical string representation
        of a polynomial.

        """
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x) -> float:
        """A method to call the polynomial
        """
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x ** index
        return res


p = Polynomial(4, 0, -4, 3, 0)
X = np.linspace(-3, 3, 50, endpoint=True)
F = p(X)
plt.plot(X, F)

plt.show()
