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
    word_list.remove('')
    word_list.sort()
    word_tuple = ([], [])
    for idx, each_str in enumerate(word_list):
        list_left = word_tuple[0]
        list_right = word_tuple[1]
        if each_str in list_left:
            if each_str == word_list[idx - 1]:
                list_right[-1] += 1
        else:
            list_left.append(each_str)
            list_right.append(1)
    print(word_tuple[0])
    print("and")
    print(word_tuple[1])
if __name__ == '__main__':
    histogram_tuples((sys.argv[1]))
