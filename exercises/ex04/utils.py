"""List utility functions."""

<<<<<<< HEAD
__author__ = "730484925"


def all(num_list: list[int], num: int) -> bool:
    """This function is used to tell if any of the functions in the list are the same  as the given list."""
    i: int = 0
    list_lenght: int = len(num_list)
    while i < list_lenght:
        if num_list[i] != num:
            return False
        else:
            i += 1
    if len(num_list) == 0:
        return False
    return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """This function is used to see if both of the lists are the exact same."""
    i: int = 0
    if len(first_list) == 0 and len(second_list) == 0:
        return True
    if len(first_list) == len(second_list):
        while i < len(first_list) and i < len(second_list):
            if first_list[i] == second_list[i]:
                return True
            else:
                i += 1
    return False


def max(max_list: list[int]) -> int:
    """This function is used to find the max of the list."""
    i: int = 1
    num: int
    greater_num = max_list[0]
    if len(max_list) == 0:
        raise ValueError("max() are is an empty list")
    while i < len(max_list):
        num = max_list[i]
        if greater_num <= num:
            greater_num = num
        i += 1
    return greater_num
=======
__author__ = "123456789"


# TODO: Implement your functions here.
>>>>>>> 6ef5547196b5cf2be3414f98dcf7f33291022ae8
