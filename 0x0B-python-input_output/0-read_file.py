#!/usr/bin/python3
"""
this is a module that reads a text file
"""
def read_file(filename=""):
    """
    this is a method that reads a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
