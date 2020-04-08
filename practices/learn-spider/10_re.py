# -*- coding: utf-8 -*-
import re


def test1():
    one = 'msdawd123124'
    two = 'a\b'
    pattern = re.compile(two)
    result = pattern.findall(one)
    print(result)


def test2():
    one = '''
    hello world
    12345 67890
    '''
    pattern = re.compile('m(.*)n', re.S | re.I)
    print(pattern.findall(one))


def test3():
    one = '123'
    pattern = re.compile('^\d+$')
    print(pattern.findall(one))


def test4():
    one = '87661'
    pattern = re.compile('[1-9]+')
    print(pattern.findall(one))


def test5():
    one = 'abc 123'
    pattern = re.compile('\d+')
    # match 从头匹配 匹配一次
    pattern.match(one)
    # search 从任意位置 , 匹配一次
    pattern.search(one)
    # findall  查找符合正则的 内容 -- list
    pattern.findall(one)
    # sub  替换字符串
    pattern.sub('#', one)
    # split  拆分
    pattern = re.compile(' ')
    print(pattern.split(one))


def test6():
    str = '我是一个粉刷匠, 我没有大鼻子'
    pattern = re.compile('[\u4e00-\u9fa5]+')
    print(pattern.findall(str))


if __name__ == '__main__':
    test6()
