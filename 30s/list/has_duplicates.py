"""
Checks a flat list for duplicate values. Returns True if duplicate values exist and False if values are all unique.

This function compares the length of the list with length of the set() of the list. set() removes duplicate values from the list.
"""
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]


def has_duplicates(lst):
    return len(lst) != len(set(lst))


if __name__ == '__main__':
    print(has_duplicates(x))  # True
    print(has_duplicates(y))  # False
