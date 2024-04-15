#!/usr/bin/python3
"""DOC"""


def print_sorted_dictionary(a_dictionary):
    """DOC"""
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
