"""
Randomizes the order of the values of an list, returning a new list.

Uses the Fisher-Yates algorithm to reorder the elements of the list.
"""
from copy import deepcopy
from random import randint

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def shuffle(lst):
    temp = deepcopy(lst)
    m = len(temp)
    while (m):
        m -= 1
        i = randint(0, m)
        temp[m], temp[i] = temp[i], temp[m]
    return temp


if __name__ == '__main__':
    print(shuffle(foo))
