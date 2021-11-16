"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
<<<<<<< HEAD
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730484925"


def test_invert() -> None:
    """This is a test for invert."""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}


def test_invert_second() -> None:
    """This is a test for invert part two."""
    assert invert({'e': 'f', 'g': 'h'}) == {'f': 'e', 'h': 'g'}


def test_invert_third() -> None:
    """This is a test for invert part three."""
    assert invert({'l': 'j', 'f': 'n'}) == {'j': 'l', 'n': 'f'}


def test_favorite_color() -> None:
    """This is a test for color part one."""
    assert favorite_color({'nick': 'blue', 'mick': 'black'}) == ['blue']


def test_favorite_color_second() -> None:
    """This is a test for color part two."""
    assert favorite_color({'nick': 'green', 'mick': 'green'}) == ['green']


def test_favorite_color_third() -> None:
    """This is a test for color part three."""
    assert favorite_color({'nick': 'blue', 'mick': 'black', 'sick': 'grey'}) == ['blue']


def test_count() -> None:
    """This is a test for the first count function."""
    assert count(["1", "2", "3", "4"]) == {"1": 1, "2": 1, "3": 1, "4": 1}


def test_count_second() -> None:
    """This is a test for the second count function."""
    assert count(["1", "2", "3"]) == {"1": 1, "2": 1, "3": 1}


def test_count_third() -> None:
    """This is a test for the third count function."""
    assert count(["1", "2", "2"]) == {"1": 1, "2": 2}
=======
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"
>>>>>>> 6ef5547196b5cf2be3414f98dcf7f33291022ae8
