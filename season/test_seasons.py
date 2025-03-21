from seasons import convert
import pytest
def main():
    test_1()
def test_1():
    assert convert("1999-01-01")=="Thirteen million, two hundred eighty-one thousand, one hundred twenty"
if __name__=="__main__":
    main()
