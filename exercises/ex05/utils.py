"""List utility functions part 2."""

__author__ = "730484925"


def only_evens(input_list: list[int]) -> list[int]:
    """This function returns the even values that are in the list provided."""
    i: int = 0
    even_list: list[int] = []
    while i < len(input_list):
        if (input_list[i] % 2) == 0:
            even_list.append(input_list[i])
        i += 1
    return even_list


def sub(set_list: list[int], first_index: int, last_index: int) -> list[int]:
    """This function returns a the values of a list between the provided start and end bounds."""
    sub_set: list[int] = []
    i: int = first_index
    if first_index < 0:
        i = 0
    if last_index > len(set_list):
        last_index = len(set_list) 
    if last_index <= 0:
        return sub_set
    while i < last_index:
        sub_set.append(set_list[i])
        i += 1
    return sub_set


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """This function adds all of the elements from the second function to the first one."""
    if len(second_list) == 0:
        return first_list
    elif len(first_list) == 0:
        return second_list
    i: int = 0
    while i < len(second_list):
        first_list.append(second_list[i])
        i += 1
    return first_list

    def test_only() -> None:
        """This test is to test only evens with an odd set and one even."""
        assert only_evens([30,23,45]) == [30]
    

    def test_evens() -> None:
        """This is to test the only evens with two evens"""
        assert only_evens([2,4,5]) == [2,4]
