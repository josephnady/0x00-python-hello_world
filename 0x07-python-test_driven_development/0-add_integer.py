#!/usr/bin/python3
"""Script to add 2 integers"""

def add_integer(a, b=98):
    """Function to add 2 integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise ValueError("a must be an integer")    
    if not isinstance(b, int) and not isinstance(b, float):
        raise ValueError("b must be an integer")
    return int(a) + int(b)
