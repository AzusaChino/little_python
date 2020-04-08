"""
Converts a string to camelcase.

Use learn-re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+". Use title() to capitalize the first letter of each word convert the rest to lowercase. Finally, use replace() to remove spaces between words.

"""

import re


def camel(s):
    s = re.sub(r'[_|-]+', ' ', s).title().replace(' ', '')
    return s[0].lower() + s[1:]


camel('Some label that needs to be camelized')  # 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property')  # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')  # 'someMixedStringWithSpacesUnderscoresAndHyphens'
# 'someDatabaseFieldName'
print(camel('some_database_field_name'))
