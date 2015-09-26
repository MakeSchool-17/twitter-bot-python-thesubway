import string


def histogram(source_text):
    my_file = open(source_text, "r")
    # my_paragraph = my_file.read()
    aSet = set(string.punctuation)
    aSet.remove('-')  # because dashes are allowed
    # aSet.remove('\\')
    adjusted_str = ''
    for line in my_file:
        adjusted_line = ''.join(ch for ch in line if ch not in aSet)
        adjusted_line = adjusted_line.replace('-', ' ')
        adjusted_line = adjusted_line.replace("\n", ' ')
        adjusted_line = adjusted_line.lower()
        adjusted_str += adjusted_line
    word_list = adjusted_str.split(' ')

    # count occurrence of strings:
    word_dict = {}
    for each_str in word_list:
        if each_str in word_dict:
            word_dict[each_str] += 1
        else:
            word_dict[each_str] = 1
    if '' in word_dict:
        del word_dict['']
    return word_dict


def unique_words(input_histogram):
    return len(input_histogram.keys())


def frequency(word, input_histogram):
    if word in input_histogram:
        print('is there')
    else:
        print('not there')

if __name__ == '__main__':
    my_dict = histogram("poker.txt")
    num_unique = unique_words(my_dict)
