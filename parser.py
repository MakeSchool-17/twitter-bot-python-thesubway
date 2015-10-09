import re
import heap


def parse_words(source_text):
    my_file = open(source_text, "r")
    # keep sentence-ending punctuation
    unwanted_punctuation = list(r'*_"}{][$^&~`')
    adjusted_str = ''
    for line in my_file:
        current_line = line.replace("\n", ' ')
        # current_line = current_line.replace('-', ' ')
        # current_line = current_line.lower()
        # .,:?!- are allowed
        adjusted_line = ''.join(ch for ch in current_line if ch not in unwanted_punctuation)
        adjusted_str += adjusted_line
    token_list = re.split('\s+', adjusted_str)
    return token_list


def histogram(source_text):
    word_list = parse_words(source_text)

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


def transfer_to_heap(dict):
    new_heap = heap.Heap()
    for key in dict:
        new_heap.insert((key, dict[key]))
    return new_heap


def print_heap(heap):
    for node in heap.nodes:
        print(node.value)

if __name__ == '__main__':
    my_dict = histogram("meaning_of_good.txt")
    my_heap = transfer_to_heap(my_dict)
    print_heap(my_heap)
    # print(my_dict)
