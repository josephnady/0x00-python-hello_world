#!/usr/bin/python3
"""DOC"""


def best_score(a_dictionary):
    """DOC"""
    if a_dictionary:
        best_score = max(a_dictionary.values())
        best_achiever = [k for k, v in a_dictionary.items() if v == best_score][0]
        return best_achiever
    else:
        return None
