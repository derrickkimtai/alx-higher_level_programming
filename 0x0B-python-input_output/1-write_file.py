#!/usr/bin/python3
"""
this is a module for opening and writing
"""


def write_file(filename="", text=""):
    """
    this is a class for writing and explain most of them
    """
    with open(filename, "w", encoding="utf-8") as f:
        integers_file = f.write(text)
    return integers_file
