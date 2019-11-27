'''
Removes falsey values from a list.
Use filter() to filter out falsey values (False, None, 0, and "").
'''


def compact(lst):
    return list(filter(bool, lst))


if __name__ == '__main__':
    print(compact([1, 2, '', 0, None]))  # [1, 2]
