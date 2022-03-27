import pytest

def num0(x):
    return x

@pytest.mark.easy
def test_num0():
    assert num0(0) == 0

def num1(x):
    return x

@pytest.mark.difficult
def test_num1():
    assert num1(1) == 1

def num2(x):
    return x

def test_num2():
    assert num2(2) == 2

def num3(x):
    return x

def test_num3():
    assert num3(3) == 3

def num4(x):
    return x

def test_num4():
    assert num4(4) == 4

def num5(x):
    return x

def test_num5():
    assert num5(5) == 5

def num6(x):
    return x

def test_num6():
    assert num6(6) == 6

def num7(x):
    return x

def test_num7():
    assert num7(7) == 7

def num8(x):
    return x

def test_num8():
    assert num8(8) == 8

def num9(x):
    return x

def test_num9():
    assert num9(9) == 9

