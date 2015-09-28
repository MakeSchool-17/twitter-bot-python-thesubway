import sys
import dan_hoang_helper


def read_histogram(file_name):
    input_file = open(file_name, 'r')
    final_dict = {}
    for line in input_file:
        adjusted_line = dan_hoang_helper.remove_linebrk(line)
        each_arr = adjusted_line.split(" ")
        final_dict[each_arr[0]] = each_arr[1]
    return final_dict

if __name__ == '__main__':
    print(read_histogram((sys.argv[1])))
