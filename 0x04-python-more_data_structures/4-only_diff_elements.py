#!/usr/bin/python3
"""DOC"""


def only_diff_elements(set_1, set_2):
    """DOC"""
    res = set()
    [res.add(x) for x in set_1 if x not in set_2]
    [res.add(y) for y in set_2 if y not in set_1]
    return (res)
