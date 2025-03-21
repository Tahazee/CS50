from jar import Jar
import pytest


def test_init():
    assert Jar().capacity==12
    assert Jar(1).capacity==1


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(6)
    assert jar._size==6


def test_withdraw():
    jar=Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar._size==3
