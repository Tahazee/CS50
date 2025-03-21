from twttr import shorten
import pytest


def test_upper():
     assert shorten("TAHA")=="TH"
def test_number():
    assert shorten("T12AHa1H")=="T12H1H"
def test_small():
     assert shorten("taha")=="th"
def test_punc():
     assert shorten("t'a,u,i.h")=="t',,.h"

