import parser

if __name__ == '__main__':
    my_dict = parser.histogram("meaning_of_good.txt")
    my_heap = parser.transfer_to_heap(my_dict)
    parser.print_heap(my_heap)
