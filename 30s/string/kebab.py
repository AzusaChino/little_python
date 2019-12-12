"""
Converts a string to kebab case.

Break the string into words and combine them adding - as a separator, using a regexp.
"""
import re


def kebab(s):
    return re.sub(r"(\s|_|-)+", "-",
                  re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                         lambda mo: mo.group(0).lower(), s)
                  )


kebab('camelCase')  # 'camel-case'
kebab('some text')  # 'some-text'
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
print(kebab('some-mixed_string With spaces_underscores-and-hyphens'))
kebab('AllThe-small Things')  # "all-the-small-things"
