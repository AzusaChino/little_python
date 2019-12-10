"""
cast_list
PythonUtilityListBeginner
Casts the provided value as an array if it's not one.

Use isinstance() to check if the given value is enumerable and return it by using list() or encapsulated in a list accordingly.
"""


def cast_list(val):
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]


cast_list('foo')  # ['foo']
cast_list([1])  # [1]
cast_list(('foo', 'bar'))  # ['foo', 'bar']

if __name__ == '__main__':
    print(cast_list([None]))
