"""Practice with dictionaries."""

__author__ = "730484925"

# Define your functions below


def invert(input_dic: dict[str, str]) -> dict[str, str]:
    """This function is meant to invert a dictionary."""
    inverse_dic: dict[str, str]
    inverse_dic = {}
    for key in input_dic:
        if input_dic[key] in inverse_dic:
            raise KeyError("KeyError")
        else: 
            inverse_dic[input_dic[key]] = key
    return inverse_dic


def favorite_color(start_dict: dict[str, str]) -> str:
    """This fucnction finds the most called color."""
    color_dic: dict[str, int]
    color_dic = {}
    max_num: int = 0
    key_set: str = ""
    for key in start_dict:
        if start_dict[key] in color_dic:
            color_dic[start_dict[key]] += 1
        else:
            color_dic[start_dict[key]] = 1
    for key in color_dic:
        if color_dic[key] > max_num:
            max_num = color_dic[key]
            key_set = key
    return key_set


def count(input_list: list[str]) -> dict[str, int]:
    """This function finds the highest count."""
    final_dic: dict[str, int]
    final_dic = {}
    for key in input_list:
        if key in final_dic:
            final_dic[key] += 1
        else:
            final_dic[key] = 1
    return final_dic
