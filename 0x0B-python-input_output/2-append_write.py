#!/usr/bin/python3
"""
this is a module to append a text at the end of a file
"""


def append_write(filename="", text=""):
    """
    this is method to append a string at the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        integers_num = f.write(text)
    return integers_num
