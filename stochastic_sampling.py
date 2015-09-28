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


def random_word_frequency(input_histogram):
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


def random_word_colorbonus(input_histogram):
    my_vals = list(input_histogram.values())
    my_keys = list(input_histogram.keys())
    enemies = 0
    winning_idx = 0
    for idx, each_val in enumerate(my_vals):
        if each_val == 0:
            continue
        multiplier = 1
        each_word = my_keys[idx]
        if each_word in ['red', 'blue', 'yellow', 'green', 'orange', 'purple']:
            multiplier = 2
        friends_lots = each_val * multiplier
        result = random.randint(1, (friends_lots + enemies))
        if result <= friends_lots:
            winning_idx = idx
        enemies += friends_lots
    return my_keys[winning_idx]

if __name__ == '__main__':
    my_file = str(sys.argv[1])
    my_histogram = word_frequency.histogram(my_file)
    # random_word = histogram_word(my_histogram)
    # print(random_word)
    # random_word = random_word_frequency(my_histogram)
    # print(random_word)

    my_results = dan_hoang_helper.test_results_parameter(10000, random_word_colorbonus, my_histogram)
    print(my_results)
