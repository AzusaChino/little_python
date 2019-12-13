"""Returns True if the provided function returns True for at least one element in the list, False otherwise.

Use any() in combination with map() and fn to check if fn returns True for any element in the list.

"""


def most_frequent(lst: list) -> int:
    return max(set(lst), key=lst.count)


print(most_frequent([1, 2, 3, 4, 54, 2, 2, 2]))
