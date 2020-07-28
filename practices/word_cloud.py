import pandas as pd
from wordcloud import WordCloud


def main():
    """
    pd读取数据, 生成词云
    """
    data = pd.read_excel(r'../')
    words = '.'.join(x for x in data['city'] if x != [])
    wc = WordCloud(

    )
    res = wc.generate(words)
    res.to_file('../resources/data.png')


if __name__ == '__main__':
    main()
