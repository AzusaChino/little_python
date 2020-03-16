'''
Already implemented via collections.Counter
Groups the elements of a list based on the given function and returns the count of elements in each group.
Use map() to map the values of the list using the given function.
Iterate over the map and increase the the elements count each time it occurs.
'''

from math import floor


def count_by(arr, fn=lambda x: x):
    key = {}
    for el in map(fn, arr):
        key[el] = 0 if el not in key else key[el]
        key[el] += 1
    return key


if __name__ == '__main__':
    print(count_by([6.1, 4.2, 6.3], floor))
    print(count_by(['one', 'two', 'three'], len))
