from plates import is_valid
import pytest

def test_alpha():
    assert is_valid("A1352")==False
    assert is_valid("As352")==True
def test_len():
    assert is_valid("AS642")==True
    assert is_valid("as6327837")==False
def test_fnum():
    assert is_valid("as083")==False
def test_schar():
    assert is_valid("as,c.d")==False
def test_middle():
    assert is_valid("AS67s")==False


