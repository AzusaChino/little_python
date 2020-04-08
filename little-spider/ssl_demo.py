import ssl
from urllib.request import Request, urlopen


def func():
    ctx = ssl.create_default_context()
    req = Request(url='http://www.baidu.com',
                  method='GET',
                  headers={'HOST': 'baidu.com'},
                  data=None)
    res = urlopen(req, context=ctx)

    headers = res.info()  # 响应头
    content = res.read()  # 响应体
    code = res.getcode()  # 状态码
