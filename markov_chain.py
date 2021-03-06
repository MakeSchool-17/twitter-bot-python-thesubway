import re
import random


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
        line_arr = re.split('\s+', adjusted_line)
        if line_arr[-1] == '':
            del line_arr[-1]
        if line_arr[0] == '':
            del line_arr[0]
        arr_str += line_arr
    token_list = arr_str
    return token_list


def histogram(word_list):
    word_dict = {}
    for idx, each_str in enumerate(word_list):
        next_word = None
        token = None
        if idx + 1 < len(word_list):
            next_word = word_list[idx + 1]
        if each_str in word_dict:
            token = word_dict[each_str]
            token.count += 1
        else:
            token = Token()
            token.count = 1
            token.name = each_str
            word_dict[each_str] = token
        if next_word is not None:
            token.followed_words.append(next_word)
    for key in word_dict:
        # tell token to update its inner_stochastic property:
        token = word_dict[key]
        token.stochastic_sample()
    return word_dict


def generate_message(markov_histogram):
    current_key = random.choice(list(markov_histogram.keys()))
    sentence_done = False
    sentence = ""
    num_words = 0
    while True:
        current_token = markov_histogram[current_key]
        current_word = current_token.name
        sentence += current_word
        num_words += 1
        if current_word[-1:] in list("."):
            sentence_done = True
        if num_words < 5:
            # keep going
            sentence_done = False
        elif num_words > 100:
            sentence_done = True
        if len(current_token.inner_stochastic) == 0:
            sentence_done = True
        if sentence_done is True:
            break
        sentence += " "
        next_key = random.choice(list(current_token.inner_stochastic.keys()))
        current_key = next_key
    return sentence


class Token:

    def __init__(self):
        self.count = None
        self.name = None
        self.followed_words = []
        self.inner_stochastic = {}

    def stochastic_sample(self):
        word_dict = {}
        for idx, each_str in enumerate(self.followed_words):
            if each_str in word_dict:
                word_dict[each_str] += 1
            else:
                word_dict[each_str] = 1
        if '' in word_dict:
            del word_dict['']
        self.inner_stochastic = word_dict

    def __str__(self):
        return str(self.count)

if __name__ == '__main__':
    my_arr = make_words("meaning_of_good.txt")
    my_histgrm = histogram(my_arr)
    # for idx, key in enumerate(my_histgrm):
    #     if idx < 10:
    #         token = my_histgrm[key]
    #         print("{0}: {1}, ".format(key, token.inner_stochastic))
    my_message = generate_message(my_histgrm)
    print(my_message)
