"""
Already implemented via itertools.zip_longest()
Creates a list of elements, grouped based on the position in the original lists.
Use max combined with list comprehension to get the length of the longest list in the arguments. Loops for max_length times grouping elements. If lengths of lists vary fill_value is used.
By default fill_value is None.
"""


def zip(*args, fillvalue=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fillvalue for k in range(len(args))
        ])
    return result


if __name__ == '__main__':
    print(zip(['a', 'b'], [1, 2], [True, False]))
    print(zip(['a'], [1, 2], [True, False]))
    print(zip(['a'], [1, 2], [True, False], fillvalue='_'))
    """
    [['a', 1, True], ['b', 2, False]]
    [['a', 1, True], [None, 2, False]]
    [['a', 1, True], ['_', 2, False]]
    """
