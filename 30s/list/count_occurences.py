'''
 Already implemented via list.count().
Counts the occurrences of a value in an list.
Uses the list comprehension to increment a counter each time you encounter the specific value inside the list.
'''


def count_occur(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])


if __name__ == '__main__':
    print(count_occur([1, 1, 2, 1, 2, 3], 1))  # 3
    print(list.count([1, 1, 2, 1, 2, 3], 1))  # 3
