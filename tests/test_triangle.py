from triangle import hypot
import numpy as np

def test_hypot():
    assert hypot(2,2) == np.sqrt(8)
    assert hypot(1,1) == np.sqrt(2)