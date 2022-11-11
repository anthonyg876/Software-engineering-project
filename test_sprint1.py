import db
import pytest



def quick(x):
    return x * 5

def test_quick():
    assert quick(10) == 50

def test_quick1():
    assert quick(1) == 5
    
def test_quick2():
    assert quick(100) == 50



