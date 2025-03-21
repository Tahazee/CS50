

from fuel import convert, gauge
import pytest
def main():
    test_convert_valid_input()
    test_convert_division_by_zero()
    test_value()


def test_convert_valid_input():
    assert convert("3/4") == 75 and gauge(75)=="75%"

    assert convert("1/4") == 25 and gauge(1)=="E"

    assert convert("4/4") == 100 and gauge(100)=="F"
    assert gauge(99)=="F"


def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()





# from fuel import convert,gauge

# import pytest
# def test_low():
#      #     assert convert("3/4") == 75 and gauge(75)=="75%"

# #     assert convert("1/4") == 25 and gauge(1)=="E"

# #     assert convert("4/4") == 100 and gauge(100)=="F"
# #     assert gauge(99)=="F"


