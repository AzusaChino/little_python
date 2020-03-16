"""
Deep flattens a list.
Use recursion递归. Use list.extend() with an empty list (result) and the spread function to flatten a list.
Recursively flatten each element that is a list.
"""


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


if __name__ == '__main__':
    print(deep_flatten([1, [2], [2, [3, [4]]], 5, [6, [6, [6], [6]]]]))  # [1, 2, 2, 3, 4, 5, 6, 6, 6, 6]
