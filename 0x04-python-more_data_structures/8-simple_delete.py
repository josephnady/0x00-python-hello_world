#!/usr/bin/python3
"""DOC"""


def simple_delete(a_dictionary, key=""):
    """DOC"""
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
