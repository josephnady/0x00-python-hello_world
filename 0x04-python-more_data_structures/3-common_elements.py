#!/usr/bin/python3
"""DOC"""


def common_elements(set_1, set_2):
    """DOC"""
    res = set()
    [res.add(x) for x in set_1 if x in set_2]
    return (res)
