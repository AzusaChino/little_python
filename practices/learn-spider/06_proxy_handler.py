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


def create_proxy_handler2():
    username = 'abc'
    password = '123'
    proxy_host = '123.158.63.130:8080'

    password_manager = request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password('', uri=proxy_host, user=username, passwd=password)
    handle_auth_proxy = request.ProxyBasicAuthHandler(password_manager)
    opener_auth = request.build_opener(handle_auth_proxy)

    response = opener_auth.open('http://www.baidu.com')
    print(response.read())


if __name__ == '__main__':
    create_proxy_handler2()
