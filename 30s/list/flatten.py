"""
Flattens a list of lists once.

Use nested list comprehension to extract each value from sub-lists in order.
"""


def flatten(lst):
    return [x for y in lst for x in y]


flatten([[12, 34, 5], [2, 2, 3]])
