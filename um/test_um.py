from um import count
import pytest


def test_one():
    assert count("UM,um,um tahaa")==3
def test_two():
    assert count("ummm,hmm")==0
def test_three():
    assert count("taha um ")==1
