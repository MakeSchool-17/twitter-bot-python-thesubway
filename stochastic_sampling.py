import sys
import word_frequency
import random
import dan_hoang_helper


def histogram_word(input_histogram):
    input_keys = list(input_histogram.keys())
    if len(input_keys) == 0:
        return ""
    my_num = random.randint(0, len(input_keys) - 1)
    return input_keys[my_num]


def histogram_weighted_word(input_histogram):
    my_vals = list(input_histogram.values())
    enemies = 0
    winning_idx = 0
    for idx, each_val in enumerate(my_vals):
        if each_val == 0:
            continue
        result = random.randint(1, (each_val + enemies))
        if result <= each_val:
            winning_idx = idx
        enemies += each_val
    my_keys = list(input_histogram.keys())
    return my_keys[winning_idx]

if __name__ == '__main__':
    my_file = str(sys.argv[1])
    my_histogram = word_frequency.histogram(my_file)
    # random_word = histogram_word(my_histogram)
    # print(random_word)
    # random_word = histogram_weighted_word(my_histogram)
    # print(random_word)

    my_results = dan_hoang_helper.test_results_1_parameter(10000, histogram_weighted_word, my_histogram)
    print(my_results)
