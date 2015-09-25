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
    return word_list


if __name__ == '__main__':
    my_arr = histogram("poker.txt")
    print(my_arr)
