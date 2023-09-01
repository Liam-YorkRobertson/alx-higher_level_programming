#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(lst):
    """
    Finds the peak.
    """
    if not lst:
        return None

    left, right = 0, len(lst) - 1

    while left < right:
        mid = (left + right) // 2

        if lst[mid] > lst[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return lst[left]
