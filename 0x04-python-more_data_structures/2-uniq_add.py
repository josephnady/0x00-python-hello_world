#!/usr/bin/python3
"""DOC"""


def uniq_add(my_list=[]):
    """DOC"""
    uniq_lst = set()
    [list(map(lambda x: uniq_lst.add(x),my_list))]
    res = sum(x for x in uniq_lst)
    return (res)