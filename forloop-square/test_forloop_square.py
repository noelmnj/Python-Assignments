import pytest
from forloopsquare import get_square_forloop

def test_get_square1():
        assert get_square_forloop([1,3,5,9]) == [1,9,25,81]

def test_get_square2():
        assert get_square_forloop([2,4,6,8]) == [4,16,36,64]


def test_get_square3():
        assert get_square_forloop([1,0,1,0]) == [1,0,1,0]

def test_get_square4():
        assert get_square_forloop([-1,-2,-3,-4]) == [1,4,9,16]
   

        '''pytest test_forloop_square.py'''