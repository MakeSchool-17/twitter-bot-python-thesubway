import sys


def get_dict_words(num_words):
    if num_words <= 0:
        return
    my_file = open('words', 'r')
    for i in range(0, num_words):
        current_str = my_file.readline()
        print(current_str)

if __name__ == '__main__':
    get_dict_words(int(sys.argv[1]))
