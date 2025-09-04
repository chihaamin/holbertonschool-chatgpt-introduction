#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is to be calculated.
                 Must be a non-negative integer.

    Returns:
        int: The factorial value of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the argument from the command line, compute factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
