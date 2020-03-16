"""
Retuns number of vowels in provided string.

Use a regular expression to count the number of vowels (A, E, I, O, U) in a string.
"""
import re


def count_vowels(string):
    return len(re.findall(r'[aiueo]', string, re.IGNORECASE))


a = count_vowels('foobar')  # 3
b = count_vowels('gym')  # 0
print(a, b)
