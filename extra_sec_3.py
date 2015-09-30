import sys
import dan_hoang_helper
import word_frequency


def read_histogram(file_name):
    input_file = open(file_name, 'r')
    final_dict = {}
    for line in input_file:
        adjusted_line = dan_hoang_helper.remove_linebrk(line)
        each_arr = adjusted_line.split(" ")
        final_dict[each_arr[0]] = each_arr[1]
    return final_dict


def histogram_tuples(source_text):
    word_list = word_frequency.get_words(source_text)
    word_list.sort()
    tuple_arr = []
    for idx, each_str in enumerate(word_list):
        # search list for tuples with 0th element == each_str
        existing_idx = None
        for inner_idx, each_tuple in enumerate(tuple_arr):
            if each_tuple[0] == each_str:
                existing_idx = inner_idx
                break
        if existing_idx is not None:
            old_tuple = tuple_arr[existing_idx]
            new_tuple = (old_tuple[0], old_tuple[1] + 1)
            tuple_arr[existing_idx] = new_tuple
        else:
            new_tuple = (each_str, 1)
            tuple_arr.append(new_tuple)
    return tuple_arr


def frequency_tuples(word, input_histogram):
    for each_tuple in input_histogram:
        if each_tuple[0] == word:
            return each_tuple[1]
            break
    return 0
if __name__ == '__main__':
    tuple_ans = histogram_tuples((sys.argv[1]))
    # print(tuple_ans)
    print(len(tuple_ans))
    print(frequency_tuples('the', tuple_ans))
