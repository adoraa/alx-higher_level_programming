#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary.keys())
    for key in sorted_k:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    pass
