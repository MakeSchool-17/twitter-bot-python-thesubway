import sys
import random


def rearrange_items():
    my_arr = sys.argv[1:]
    final_ans = ""
    while len(my_arr) > 0:
        my_idx = random.randint(0, len(my_arr)-1)
        current_str = my_arr[my_idx]
        final_ans += current_str
        my_arr.remove(current_str)
        if len(my_arr) > 0:
            final_ans += " "
    print(final_ans)

if __name__ == '__main__':
    rearrange_items()
