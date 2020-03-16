"""
Returns False if the provided function returns True for at least one element in the list, True otherwise.

Use all() and fn to check if fn returns False for all the elements in the list.
"""


def none(lst, fn=lambda x: x):
    return all(not fn(x) for x in lst)


none([0, 1, 2, 0], lambda x: x >= 2)
none([0, 0, 0])
