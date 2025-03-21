from numb3rs import validate
import pytest
def test_one():
    assert validate("255.255.255.255")==True
def test_three():
    assert validate("1.2.3.3")==True

def test_first_byte():
    assert validate("255.0.0.0") == True  # Valid IPv4 address with first byte in range
    assert validate("255.256.783.287") == False  # Invalid IPv4 address with first byte out of range
