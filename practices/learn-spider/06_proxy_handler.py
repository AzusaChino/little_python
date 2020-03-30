from urllib import request


def create_proxy_handler():
    url = 'http://www.baidu.com'
    proxy = {
        'http': '192.168.11.145:3128'
    }
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    res = opener.open(url).read()
    print(res)


if __name__ == '__main__':
    create_proxy_handler()
