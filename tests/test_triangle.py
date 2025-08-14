from mygeopy.triangle import hypot
from math import sqrt

def test_hypot():
    assert hypot(2,2) == sqrt(8)
    assert hypot(1,1) == sqrt(2)