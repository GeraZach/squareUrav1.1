from functions import *
from fractions import Fraction


def func(a):
    return a * 2

def test_a_is_zero():
    assert a_is_zero(4, 4) == -1.0

def test_func():
    assert func(5) == 10