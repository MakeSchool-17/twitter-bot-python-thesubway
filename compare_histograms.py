from linked_list import *
import timeit
import dan_hoang_helper
import extra_sec_3
import word_frequency


def histogram(source_text):
    word_list = word_frequency.get_words(source_text)

    # count occurrence of strings:
    word_data_struct = Linked_List()
    for each_str in word_list:
        # if each_str in word_dict:
        each_node = word_data_struct.find_node_tuple(each_str)
        if each_node is not None:
            each_node.value = (each_node.value[0], each_node.value[1] + 1)
        else:
            # word_dict[each_str] = 1
            new_value = (each_str, 1)
            new_node = Node(new_value)
            word_data_struct.unshift(new_node)
    return word_data_struct


def get_words(source_text):
    my_file = open(source_text, "r")
    # note: later code will set uppercase char to lowercase
    aSet = list("abcdefghijklm' nopqrstuvwxyz")
    adjusted_str = ''
    for line in my_file:
        current_line = line.replace("\n", ' ')
        current_line = current_line.replace('-', ' ')
        current_line = current_line.lower()
        adjusted_line = ''.join(ch for ch in current_line if ch in aSet)
        adjusted_str += adjusted_line
    final_arr = adjusted_str.split(' ')
    final_arr.remove('')
    return final_arr


def unique_words(input_histogram):
    return input_histogram.length


def frequency(word, input_histogram):
    result_node = input_histogram.find_node_tuple(word)
    if result_node is not None:
        return result_node.value[1]
    else:
        return 0


def time_function(num_times, function_name, word, input_histogram, input_type):
    start_time = timeit.default_timer()
    dan_hoang_helper.test_results_parameter(num_times, function_name, word, input_histogram)
    elapsed = timeit.default_timer() - start_time
    print(input_type + "\t\t: " + str(elapsed))


def time_many_funcs(num_times, word, list_histograms, list_funcs, input_types):
    for idx, each_function in enumerate(list_funcs):
        time_function(num_times, each_function, word, list_histograms[idx], input_types[idx])


def compare_structures_using_file(input_file):
    histogram_linked_list = histogram(input_file)
    frequency_linked = frequency
    histogram_tuples = extra_sec_3.histogram_tuples(input_file)
    frequency_tuples = extra_sec_3.frequency_tuples
    histogram_dict = word_frequency.histogram(input_file)
    frequency_dict = word_frequency.frequency

    three_functions = [frequency_linked, frequency_tuples, frequency_dict]
    three_hgrms = [histogram_linked_list, histogram_tuples, histogram_dict]
    three_types = ["linked_list", "tuples", "dictionary"]
    time_many_funcs(20000, 'loremipsum', three_hgrms, three_functions, three_types)

if __name__ == '__main__':
    hundred_words = list(range(1, 100))
    ten_thousand_words = list(range(1, 10000))
    compare_structures_using_file(hundred_words)
    compare_structures_using_file(ten_thousand_words)
