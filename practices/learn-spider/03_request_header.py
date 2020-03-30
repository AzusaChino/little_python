from urllib import request


def load_url():
    url = 'http://www.baidu.com'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36 '
    }
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/69.0.3497.100 Safari/537.36 ')

    res = request.urlopen(req)
    print(res)

    data = res.read().decode('utf-8')

    final_url = req.get_full_url()
    print(final_url)

    req_header = req.get_header('User-Agent')
    print(req_header)


if __name__ == '__main__':
    load_url()
