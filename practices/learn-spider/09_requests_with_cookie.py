import random

import requests
from common import headers


def main():
    cookies = {}

    res = requests.get('', headers=random.choice(headers), cookies=cookies)

    print(res)
    data = res.content.decode()

    with open('cookie.html', 'wd') as f:
        f.write(data)


def login():
    member_url = 'https://www.yaozh.com/member/'

    login_url = 'https://www.yaozh.com/login'
    login_form_data = {
        'username': 'xiaomaoera12',
        'pwd': 'lina081012',
        'formhash': '54AC1EE419',
        'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F',
    }
    session = requests.sessions.session()
    # 1.代码登录
    res = session.post(login_url, headers=random.choice(headers), data=login_form_data, )

    print(res.content.decode())
    # 2.登录成功之后 带着 有效的cookies 访问 请求目标数据
    data = session.get(member_url, headers=random.choice(headers)).content.decode()

    with open('session.html', 'wd') as f:
        f.write(data)
