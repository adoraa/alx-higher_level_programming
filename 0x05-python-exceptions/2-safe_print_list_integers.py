#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_ints = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_ints += 1
    except (ValueError, TypeError):
        pass
    print()
    return printed_ints
