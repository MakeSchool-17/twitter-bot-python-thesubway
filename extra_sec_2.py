import extra_sec_1
import dictionary_words
import sys


def anagram_generator(word):
    dict_list = dictionary_words.get_dict_list()
    real_words = []
    all_combinations = extra_sec_1.retrieve_str_combinations(word)
    for each_combination in all_combinations:
        for each_word in dict_list:
            if each_combination == each_word:
                real_words.append(each_combination)
                break
    return real_words


def autocomplete_front(str):
    if len(str) <= 0:
        return []
    dict_list = dictionary_words.get_dict_list()
    valid2 = []
    for each_word in dict_list:
        if str in each_word[:len(str)]:
            valid2.append(each_word)
    return valid2


if __name__ == '__main__':
    print(autocomplete_front((sys.argv[1])))
