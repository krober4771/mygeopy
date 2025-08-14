import numpy as np
import numbers

def hypot(a :float,b :float):
    """
    Compute the hypotenuse of a right triangle.

    Args:
        a (float): Length of one side next to the right angle
        b (float): Length of other side next to the right angle

    Returns:
        float: Length of the hypotenuse

    Examples:
        >>> hypot(3, 4)   # <--- Also can be a test
        5.0
    """
    
    if not (isinstance(a,numbers.Real) and isinstance(b,numbers.Real)):
        raise TypeError("'a' and 'b' must be real")
    if not (a>0 and b>0):
        raise TypeError("'a' and 'b' must be positive")
    
    return (a**2 + b**2) ** 0.5 