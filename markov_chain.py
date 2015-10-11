import re


class Token:

    def __init__(self):
        self.next = None


def make_words(source_text):
    my_file = open(source_text, "r")
    # keep sentence-ending punctuation
    unwanted_punctuation = list(r'*_"}{][$^&~`')
    arr_str = []
    for line in my_file:
        current_line = line.replace("\n", ' ')
        # current_line = current_line.replace('-', ' ')
        # current_line = current_line.lower()
        # .,:?!- are allowed
        adjusted_line = ''.join(ch for ch in current_line if ch not in unwanted_punctuation)
        arr_str += re.split('\s+', adjusted_line)
    token_list = arr_str
    return token_list


def histogram(word_list):
    word_dict = {}
    for idx, each_str in enumerate(word_list):
        if each_str in word_dict:
            word_dict[each_str] += 1
        else:
            word_dict[each_str] = 1
    if '' in word_dict:
        del word_dict['']
    return word_dict

if __name__ == '__main__':
    my_arr = make_words("meaning_of_good.txt")
    print(histogram(my_arr))
