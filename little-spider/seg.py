import random
import time

import requests
from bs4 import BeautifulSoup

from common import headers, Mysql


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
        return self.articles


def create_sql(title, context=' ', content=' '):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return 'insert into segment(id, title, context, content, create_time) values ({},{},{},{})' \
        .format(title, context, content, date)


if __name__ == '__main__':
    s = seg()
    db = Mysql()
    for article in s.get_content():
        sql = create_sql(article['title'], article['context'], article['content'])
        db.execute(sql)
