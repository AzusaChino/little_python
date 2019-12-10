"""
bifurcate
PythonListIntermediate
Splits values into two groups. If an element in filter is True, the corresponding element in the collection belongs to the first group; otherwise, it belongs to the second group.

Use list comprehension and enumerate() to add elements to groups, based on filter.
"""


def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]


if __name__ == '__main__':
    print(bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]))
