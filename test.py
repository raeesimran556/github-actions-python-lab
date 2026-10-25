
from app import add_numbers, greet


def test_add_numbers():
    assert add_numbers(5, 3) == 8


def test_negative_numbers():
    assert add_numbers(-2, 5) == 3


def test_greeting():
    assert greet("Student") == "Hello, Student!"


def test_zero():
    assert add_numbers(0, 0) == 0
