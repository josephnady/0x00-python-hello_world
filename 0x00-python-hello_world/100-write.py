#!/usr/bin/python3
import sys


def my_print():
    """function that use sys write to print"""
    sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
    exit(1)


my_print()
