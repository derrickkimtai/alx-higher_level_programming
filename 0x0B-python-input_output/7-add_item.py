#!/usr/bin/python3
"""
this the impelementation of json
"""
import json
import sys
"""
this is the importation of json
"""


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    creates an object from a "JSON file"
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data

existing_list = []

for arg in sys.argv[1:]:
    existing_list.append(arg)
save_to_json_file(existing_list, "add_item.json")
