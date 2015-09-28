import extra_sec_1
import dictionary_words


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


if __name__ == '__main__':
    print(anagram_generator('tac'))
