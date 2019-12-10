"""
union_by
PythonListFunctionIntermediate
Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

Create a set by applying fn to each element in a, then use list comprehension in combination with fn on b to only keep values not contained in the previously created set, _a. Finally, create a set from the previous result and a and transform it into a list
"""
from math import floor


def union_by(a, b, fn):
    _a = set(map(fn, a))
    return list(set(a + [item for item in b if fn(item) not in _a]))


if __name__ == '__main__':
    print(union_by([2, 1], [1.2, 2.3], floor))
