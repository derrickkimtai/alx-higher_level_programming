#!/usr/bin/python3
"""
this the importation of json module
"""
import json
"""
this the impelementing of json import
"""


def load_from_json_file(filename):
    """
    creates an object from a "JSON file"
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
