import string


def histogram(source_text):
    my_file = open(source_text, "r")
    # note: later code will set uppercase char to lowercase
    aSet = list("abcdefghijklm' nopqrstuvwxyz")
    adjusted_str = ''
    for line in my_file:
        current_line = line.replace("\n", ' ')
        current_line = current_line.replace('-', ' ')
        current_line = current_line.lower()
        adjusted_line = ''.join(ch for ch in current_line if ch in aSet)
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
        return input_histogram[word]
    else:
        return 0

if __name__ == '__main__':
    my_dict = histogram("poker.txt")
    print('data: '+str(my_dict))
    num_unique = unique_words(my_dict)
    print("num unique: "+str(num_unique))
    tested_word = "played"
    frequency_result = frequency(tested_word, my_dict)
    print(tested_word+": "+str(frequency_result))
