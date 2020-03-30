from urllib import request


def handler_opener(url):
    # 系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能
    # 安全 套接层 ssl第三方的CA数字证书
    # http80端口# 和https443
    handler = request.HTTPHandler()
    opener = request.build_opener(handler)
    res = opener.open(url)
    print(res.read())


if __name__ == '__main__':
    handler_opener('http://www.baidu.com')
