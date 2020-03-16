"""
Decapitalizes the first letter of a string.

Decapitalizes the fist letter of the sring and then adds it with rest of the string. Omit the upper_rest parameter to keep the rest of the string intact, or set it to true to convert to uppercase.
"""


def decapitalize(string, upper_rest=False):
    return string[:1].lower() + string[1:].upper() if upper_rest else string[1:]


decapitalize('FooBar')  # 'fooBar'
decapitalize('FooBar', True)  # 'fOOBAR'
