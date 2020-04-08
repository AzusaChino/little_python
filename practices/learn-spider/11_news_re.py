# -*- coding: utf-8 -*-
import re

import requests


def main():
    url = 'https://news.qq.com'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.77 Safari/537.36 '
    }
    data = requests.get(url, headers=headers).content.decode()

    # pattern = re.compile('<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>')
    pattern = re.compile('<a href="(.*?)" target="_blank">(.*?)</a>')
    print(pattern.findall(data))


if __name__ == '__main__':
    main()
