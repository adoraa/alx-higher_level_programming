#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    return {key: val for key, val in a_dictionary.items() if val != value}


def print_sorted_dictionary(new_dict):
    if not new_dict:
        return
    for key in sorted(new_dict.keys()):
        print("{}: {}".format(key, new_dict[key]))
    print("--")
