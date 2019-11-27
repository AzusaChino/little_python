"""
Returns the difference between two list, after applying the provided function to each list element of both.

Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values not contained in the previously created set.
"""
from math import floor


def difference_by(a, b, fn=lambda x: x):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


if __name__ == '__main__':
    print(difference_by([2.1, 1.2], [2.3, 3.4], floor))  # [1.2]
    print(difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x']))  # {'x':2}
