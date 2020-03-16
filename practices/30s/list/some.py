"""
Returns True if the provided function returns True for at least one element in the list, False otherwise.

Use any() in combination with map() and fn to check if fn returns True for any element in the list.
"""


def some(lst, fn=lambda x: x):
    return any(map(fn, lst))


some([0, 0, 1, 2], lambda x: x >= 2)
some([0, 2, 1, 2, 3])
