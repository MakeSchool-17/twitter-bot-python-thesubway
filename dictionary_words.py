import sys
import random


def get_dict_words(num_words):
    if num_words <= 0:
        return ""
    my_file = open('words', 'r')
    all_words = []
    final_arr = []
    final_str = ""
    for line in my_file:
        all_words.append(line)
    for i in range(0, num_words):
        my_rand_idx = random.randint(0, len(all_words)-1)
        current_word = all_words[my_rand_idx]
        # adjust word to remove the \n (last word also has \n)
        adjusted_word = current_word[:-1]
        final_arr.append(adjusted_word)
        all_words.remove(current_word)
    for each_word in final_arr:
        final_str += " " + each_word
    if num_words > 0:
        final_str = final_str[1:]
    return final_str
if __name__ == '__main__':
    my_sentence = get_dict_words(int(sys.argv[1]))
    print(my_sentence)
