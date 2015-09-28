import sys


def remove_new_line(input_str):
    final_arr = input_str.splitlines()
    final_str = "".join(final_arr)
    return final_str
