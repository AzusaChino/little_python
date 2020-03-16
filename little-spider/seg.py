import random
import time

import pymysql
import requests
from bs4 import BeautifulSoup

from common import headers


class seg(object):

    def __init__(self):
        self.base_url = "https://segmentfault.com"
        self.headers = headers
        self.articles = []

    def get_content(self):
        r = requests.get(self.base_url, headers={'user-agent': random.choice(self.headers)})
        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.find_all('div', class_='news__item-info')
        for i in items:
            i_title = i.find('h4', class_='news__item-title').text
            i_context = i.find('div', class_='article-excerpt').text
            i_link = i.find('a').get('href')
            i_r = requests.get(self.base_url + i_link, headers={'user-agent': random.choice(self.headers)})
            i_soup = BeautifulSoup(i_r.text, 'lxml')
            i_ps = i_soup.find('div', class_='article').find_all('p')
            i_content = ''
            for i_p in i_ps:
                if i_p.text is not None:
                    i_content += i_p.text + '\r\n'
            self.articles.append({'title': i_title, 'context': i_context,
                                  'link': self.base_url + i_link, 'content': i_content})


def create_sql(title, context=' ', content=' '):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return """insert into segment(title, context, content, date) values ('%s','%s','%s','%s') """ % (
        title, context, content, date)


class db(object):

    def __init__(self):
        self.db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='azusa520', db='chino',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def execute(self, sql):
        try:
            # 执行语句
            self.cursor.execute(sql)
            # 提交到数据库
            self.db.commit()
        except:
            self.db.rollback()
            print("error happened")


if __name__ == '__main__':
    s = seg()
    db = db()
    s.get_content()
    for article in s.articles:
        sql = create_sql(article['title'], article['context'], article['content'])
        db.execute(sql)
