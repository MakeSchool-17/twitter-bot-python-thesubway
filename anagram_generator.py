import dictionary_words


def anagram_generator(word):
    dict_list = dictionary_words.get_dict_list()
    real_words = []
    all_combinations = retrieve_str_combinations(word)
    for each_combination in all_combinations:
        for each_word in dict_list:
            if each_combination == each_word:
                real_words.append(each_combination)
                print("got here")
                break
    print(len(all_combinations))
    print(len(dict_list))
    return real_words


def retrieve_str_combinations(input_str):
    if input_str == "":
        return []
    if len(input_str) == 1:
        return [input_str]
    input_list = list(input_str)
    recursive_list = []
    for idx, val in enumerate(input_list):
        temp_list = input_list[:]
        first_letter = input_list[idx]
        del temp_list[idx]
        remainder = "".join(temp_list)
        temp_word = first_letter + remainder
        # next, iterate through temp_word
        inner_list = retrieve_str_combinations(remainder)
        for each_inner in inner_list:
            inner_word = first_letter + each_inner
            recursive_list.append(inner_word)
    return recursive_list


if __name__ == '__main__':
    # anagram_generator('tacs')
    print(anagram_generator('tac'))
