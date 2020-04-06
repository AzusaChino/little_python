import requests


def main(url: str):
    data = {}
    auth = ('username', 'password')
    proxies = {'http': '27.17.25.222:2131'}
    # ssl
    # verify: (optional) Either a boolean, in which case it controls whether we verify
    #             the server's TLS certificate, or a string, in which case it must be a path
    #             to a CA bundle to use. Defaults to ``True``.
    res = requests.get(url, data=data, auth=auth, proxies=proxies, verify=False)
    print(res)
