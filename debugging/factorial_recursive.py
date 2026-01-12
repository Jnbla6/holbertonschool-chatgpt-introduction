#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description: 
    Calculates the factorial of a given number using recursion.

    Parameters:
    n: The integer to calculate the factorial of.

    Returns:
    The factorial value of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
