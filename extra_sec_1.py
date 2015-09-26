def string_reversal(my_str):
    if my_str == "":
        return ""
    else:
        str_list = list(my_str)
        new_list = []
        for each_char in str_list:
            new_list.insert(0, each_char)
        return "".join(new_list)

if __name__ == '__main__':
    reversed_str = string_reversal("my string")
    print(reversed_str)
