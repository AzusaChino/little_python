import jieba


# jieba.enable_paddle()


def test(s):
    return jieba.cut(s, cut_all=True)


if __name__ == '__main__':
    l = test("这是一个句子")
    print("/".join(l))
