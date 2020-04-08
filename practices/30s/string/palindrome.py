"""
Returns True if the given string is a palindrome, False otherwise.

Convert string str.lower() and use learn-re.sub to remove non-alphanumeric characters from it. Then compare the new string to the reversed.
"""
from re import sub


def palindrome(string):
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]


palindrome('taco cat')  # True
print(palindrome('tacat'))
