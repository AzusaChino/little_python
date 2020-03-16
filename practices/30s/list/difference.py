"""
Returns the difference between two iterables.
Use list comprehension to only keep values not contained in b
"""


def difference(a, b):
    return [item for item in a if item not in b]


if __name__ == '__main__':
    print(difference([1, 2, 3], [2, 3, 4, 5, 6, 7, 8]))  # [1]
