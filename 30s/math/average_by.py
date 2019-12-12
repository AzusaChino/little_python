def average_by(lst, fn=lambda x: x):
    return sum(map(fn, lst), 0.0) / len(lst)


print(average_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda x: x['n']))
