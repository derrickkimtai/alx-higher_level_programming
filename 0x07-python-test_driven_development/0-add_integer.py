#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two numbers a and b, which must be an integer or floats

    parameters:
    a (int or float): the first numbers
    b (int or float, optional): the second number. Default is 98.

    returns:
    int : the sum of a and b
     raises:
     TypeError: If a or b is not an integer or float with specific error
     """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    result = a + b
    return int(result)
