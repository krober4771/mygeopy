def test_hypot1():
    assert hypot(2,2) == np.sqrt(8)
    assert hypot(1,1) == np.sqrt(2)
    assert hypot(0,0) == 0