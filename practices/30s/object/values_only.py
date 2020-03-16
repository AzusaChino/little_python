"""
Function which accepts a dictionary of key value pairs and returns a new flat list of only the values.

Uses the .items() function with a for loop on the dictionary to track both the key and value of the iteration and returns a new list by appending the values to it. Best used on 1 level-deep key:value pair dictionaries and not nested data-structures.
"""


def keys_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(v)
    return lst


if __name__ == '__main__':
    print(keys_only({1: "2", 2: "3"}))
