#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def find_peak_recursive(lst, left, right):
        mid = (left + right) // 2
        if (mid == 0 or lst[mid] >= lst[mid - 1]) and \
           (mid == len(lst) - 1 or lst[mid] >= lst[mid + 1]):
            return lst[mid]
        elif mid > 0 and lst[mid - 1] > lst[mid]:
            return find_peak_recursive(lst, left, mid - 1)
        else:
            return find_peak_recursive(lst, mid + 1, right)

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
