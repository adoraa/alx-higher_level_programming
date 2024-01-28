#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 1 or n > len(s):
        return s
    return s[:n-1] + s[n:]
