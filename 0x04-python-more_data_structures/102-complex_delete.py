#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    return {key: val for key, val in a_dictionary.items() if val != value}


def print_sorted_dictionary(a_dict):
    if not a_dict:
        return
    for key in sorted(a_dict.keys()):
        print("{}: {}".format(key, a_dict[key]))
    print("--")
