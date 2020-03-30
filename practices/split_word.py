import re

import jieba


# jieba.enable_paddle()


def test(s):
    return jieba.cut(s, cut_all=True)


def test2(s):
    p = re.compile(r'^\s')
    print(p.match(s))


if __name__ == '__main__':
    # l = test("这是一个句子")
    # print("/".join(l))
    test2('abcd***aaa2131245:(***^%$')
