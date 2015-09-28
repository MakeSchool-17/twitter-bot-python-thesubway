import sys
import random


def get_dict_words(num_words):
    if num_words <= 0:
        return ""
    final_arr = []
    final_str = ""
    all_words = get_dict_list()
    for i in range(0, num_words):
        my_rand_idx = random.randint(0, len(all_words)-1)
        current_word = all_words[my_rand_idx]
        final_arr.append(current_word)
        all_words.remove(current_word)
    for each_word in final_arr:
        final_str += " " + each_word
    if num_words > 0:
        final_str = final_str[1:]
    return final_str


def get_dict_list():
    my_file = open('words', 'r')
    all_words = []
    for line in my_file:
        # adjust word to remove the \n (last word also has \n)
        adjusted_word = line[:-1]
        all_words.append(adjusted_word)
    return all_words
if __name__ == '__main__':
    my_sentence = get_dict_words(int(sys.argv[1]))
    print(my_sentence)
