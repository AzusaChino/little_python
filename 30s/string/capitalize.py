"""
Capitalizes the first letter of a string.

Capitalizes the fist letter of the string and then adds it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to true to convert to lowercase.
"""


def capitalize(string, lower_rest=False):
    return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])


a = capitalize('fooBar')  # 'FooBar'
b = capitalize('fooBar', True)  # 'Foobar'
print(a, b)
