"""
Clamps num within the inclusive range specified by the boundary values a and b.

If num falls within the range, return num. Otherwise, return the nearest number in the range.
"""


def clamp_number(num, a, b):
    return max(min(num, max(a, b)), min(a, b))
