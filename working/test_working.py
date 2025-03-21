from working import convert
import pytest
def main():
    test_one()
    test_four()

def test_one():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("10 PM to 8:30 AM")=="22:00 to 08:30"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
def test_four():
    with pytest.raises(ValueError):
        convert("10:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("10 AM - 5 PM")



