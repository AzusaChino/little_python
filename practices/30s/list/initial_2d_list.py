"""
initialize_2d_list
PythonListIntermediate
Initializes a 2D list of given width and height and value.

Use list comprehension and range() to generate h rows where each is a list with length h, initialized with val. If val is not provided, default to None.
"""


def initialize_2d_list(w, h, val=None):
    return [[val for _ in range(w)] for _ in range(h)]


if __name__ == '__main__':
    print(initialize_2d_list(2, 2, 0))
