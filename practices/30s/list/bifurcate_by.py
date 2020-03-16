"""
bifurcate_by
PythonListFunctionIntermediate
Splits values into two groups according to a function, which specifies which group an element in the input list belongs to. If the function returns True, the element belongs to the first group; otherwise, it belongs to the second group.

Use list comprehension to add elements to groups, based on fn.
"""
from functools import reduce


def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


if __name__ == '__main__':
    lst = ['beep', 'fi', 'fa']
    print(bifurcate_by(lst, lambda x: x[0] == 'b'))
    print(reduce(lambda x: x[0] == 'b', lst))
