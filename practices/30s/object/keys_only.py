"""
Checks a flat list for all unique values. Returns True if list values are all unique and False if list values aren't all unique.

This function compares the length of the list with length of the set() of the list. set() removes duplicate values from the list.
"""


def keys_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(k)
    return lst


if __name__ == '__main__':
    print(keys_only({1: "2", 2: "3"}))
