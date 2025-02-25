import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))
import calculator as calc


#import calculator 


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 7) == -7

def test_multiply():
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    with pytest.raises(ValueError):
        calc.divide(5, 0)
