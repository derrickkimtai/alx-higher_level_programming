#!/usr/bin/python3
"""
    this has no importation of a module in any case below
"""


def class_to_json(obj):
    """
    returns the dictionary with simple data structure
    """
    json_dict = {}

    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)

            if isinstance(attr_value, (str, int, bool)):
                json_dict[attr_name] = attr_value
            elif isinstance(attr_value, (str, int, bool)):
                serializable_items = [item for item in attr_value if isinstance(item, (str, int, bool))]
                if serializable_items:
                    json_dict[attr_name] = serializable_items
            elif isinstance(attr_value, dict):
                serializable_dict = {k: v for k, v in attr_value.items() if isinstance(v, (str, int, bool))}
                if serializable_dict:
                    json_dict[attr_name] = serializable_dict

    return json_dict
