#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()

    for item in set_1:
        if item not in set_2:
            diff_set.add(item)

    for item in set_2:
        if item not in set_1:
            diff_set.add(item)

    return diff_set
