from urllib import request, parse
import string


def get_method_params() -> None:
    url = 'http://www.baidu.com/s?wd={}'

    key_word = '智乃'

    print(url.format(key_word))

    encoded_new_url = parse.quote(url.format(key_word), safe=string.printable)

    print(encoded_new_url)

    res = request.urlopen(encoded_new_url)
    print(res)
    # 读取内容
    data = res.read().decode()
    print(data)
    # 保存到本地
    with open("02-encode.html", "w", encoding="utf-8")as f:
        f.write(data)
    # UnicodeEncodeError: 'ascii' codec can't encode
    # characters in position 10-11: ordinal not in range(128)
    # python:是解释性语言;解析器只支持 ascii 0 - 127
    # 不支持中文


if __name__ == '__main__':
    get_method_params()
