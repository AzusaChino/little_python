from urllib import request


def proxy_user(url: str) -> None:
    proxies = [
        {'http': '192.168.11.145:3128'},
        {}
    ]
    for proxy in proxies:
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)

        try:
            opener.open(url, timeout=1)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    baidu = 'https://www.baidu.com'
    proxy_user(baidu)
