def parse_words(source_text):
    my_file = open(source_text, "r")
    unwanted_punctuation = list("*_")
    adjusted_str = ''
    for line in my_file:
        current_line = line.replace("\n", ' ')
        # current_line = current_line.replace('-', ' ')
        current_line = current_line.lower()
        adjusted_line = ''.join(ch for ch in current_line if ch not in unwanted_punctuation)
        adjusted_str += adjusted_line
    final_arr = adjusted_str.split(' ')
    final_arr.remove('')
    return final_arr
