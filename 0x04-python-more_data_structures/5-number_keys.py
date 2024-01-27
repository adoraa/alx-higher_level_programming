#!/usr/bin/python3
def number_keys(a_dictionary):
    num = len(a_dictionary)
    return num


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    n_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(n_keys))
