import sys
import word_frequency
import random


def histogram_word(input_histogram):
    input_keys = list(input_histogram.keys())
    if len(input_keys) == 0:
        return ""
    my_num = random.randint(0, len(input_keys)-1)
    return input_keys[my_num]

if __name__ == '__main__':
    my_file = str(sys.argv[1])
    my_histogram = word_frequency.histogram(my_file)
    random_word = histogram_word(my_histogram)
    print(random_word)
