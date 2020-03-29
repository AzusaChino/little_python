from urllib import request


def load_data() -> None:
    url = 'https://baidu.com'
    res = request.urlopen(url)
    print(res)

    data = res.read()
    print(data)
    data_str = data.decode('utf-8')
    print(data_str)
    with open('baidu.html', 'w', encoding='utf-8') as f:
        f.write(data)

    # python爬取的类型:str bytes
    # 如果爬取回来的是bytes类型:但是你写入的时候需要字符串 decode("utf-8")
    # 如果爬取过来的是str类型:但你要写入的是bytes类型 encode(""utf-8")
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(bytes_name)


if __name__ == '__main__':
    load_data()
