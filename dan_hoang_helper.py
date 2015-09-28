import sys


def remove_new_line(input_str):
    final_arr = input_str.splitlines()
    final_str = "".join(final_arr)
    return final_str


def test_results_1_parameter(num_tests, input_function, first_param):
    my_results = {}
    for value in range(num_tests):
        result = input_function(first_param)
        if result in my_results:
            my_results[result] += 1
        else:
            my_results[result] = 1
    return my_results
