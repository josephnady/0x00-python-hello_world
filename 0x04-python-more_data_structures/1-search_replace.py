#!/usr/bin/python3
"""DOC"""


def search_replace(my_list, search, replace):
    """DOC"""
    list2 = [replace if x == search else x for x in my_list]
    return (list2)
