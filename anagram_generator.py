import dictionary_words


def anagram_generator(word):
    dict_list = dictionary_words.get_dict_list()
    real_words = []
    input_arr = list(word)
    print(len(dict_list))
    print(input_arr)
    # to get every scramble. #tac act cat cta tca atc
    combinations_arr = []


def retrieve_str_combinations(input_str):
    if input_str == "":
        return ""
    if len(input_str) == 1:
        return input_str
    input_list = list(input_str)
    print(input_list)
    recursive_list = []
    for idx, val in enumerate(input_list):
        temp_list = input_list[:]
        print(temp_list)
        first_letter = input_list[idx]
        del temp_list[idx]
        temp_word = first_letter.join(temp_list)
        recursive_list.append(temp_word)
    return recursive_list


if __name__ == '__main__':
    # anagram_generator('tacs')
    print(retrieve_str_combinations('tac'))
