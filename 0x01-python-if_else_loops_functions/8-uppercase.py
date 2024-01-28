#!/usr/bin/python3
def uppercase(s):
    for c in s:
        diff = ord('a') - ord('A')
        cap_c = chr(ord(c) - diff) if 'a' <= c <= 'z' else c
        print("{}".format(cap_c), end='')
    print()
