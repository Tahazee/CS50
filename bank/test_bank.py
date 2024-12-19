import pytest
from bank import value

def test_hello():
    assert value("hello")==0

def test_h():
    assert value("Hey")==20
def test_noh():
    assert value(" shjfhjsf")==100

