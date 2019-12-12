"""
Splits a multiline string into a list of lines.

Use s.split() and '\n' to match line breaks and create a list.
"""


def split_lines(s):
    return s.split('\n')


split_lines('This\nis a\nmultiline\nstring.\n')  # 'This\nis a\nmultiline\nstring.\n'
