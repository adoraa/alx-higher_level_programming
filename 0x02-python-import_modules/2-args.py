#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    suffix = 's' if argc > 1 else ''
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, suffix))
        if argc == 1:
            print("1: {}".format(argv[1]))
        else:
            for i, arg in enumerate(argv[1:], 1):
                print("{}: {}".format(i, arg))
