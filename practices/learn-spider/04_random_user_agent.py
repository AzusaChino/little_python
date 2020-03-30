from common import headers
from urllib import request
import random


def load_url(url: str) -> None:
    random_user_agent = random.choice(headers)

    req = request.Request(url)
    req.add_header('User-Agent', random_user_agent)

    res = request.urlopen(req)
    print(res.read())

    print(req.get_header('User-Agent'.capitalize()))


if __name__ == '__main__':
    load_url("http://www.baidu.com")
