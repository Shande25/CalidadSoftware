
import pytest
from calculadora import suma, division




@pytest.mark.parametrize("a,b, esperando", [
    (2,3,5),
    (-1,1,-2),
    (0,0,0)
]) 

def test_suma(a,b, esperando):
    assert suma(a,b) == esperando



def test_suma():
    assert suma(4,6) == 10
    assert suma(-5,4) == -1
    assert suma(0,0) == 0



def test_division():
    assert division(10,2) == 5
    assert division(9,3) == 3
    with pytest.raises(ValueError): 
        division(10,0)