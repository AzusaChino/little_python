# -*- coding:UTF-8 -*-
import random
import time

import requests
from bs4 import BeautifulSoup

from common import headers, Mysql


class downloader(object):

    def __init__(self):
        self.tab_urls = []
        self.url = 'https://www.v2ex.com'
        self.info = []
        self.headers = headers

    def get_tabs(self):
        r = requests.get(url=self.url, headers={'user-agent': random.choice(self.headers)})
        soup = BeautifulSoup(r.text, 'lxml')
        tabs = soup.find_all('div', id='Tabs')
        a = tabs[0].find_all('a')
        for each in a:
            self.tab_urls.append(self.url + each.get('href'))

    def get_info(self):
        for url in self.tab_urls:
            r = requests.get(url=url, headers={'user-agent': random.choice(self.headers)})
            soup = BeautifulSoup(r.text, 'lxml')
            cells = soup.find_all('div', class_='cell item')
            tab = soup.find('div', id='Tabs').find('a', class_='tab_current').text
            for cell in cells:
                title = cell.find('span', class_='item_title').a.text
                c_url = self.url + cell.find('span', class_='item_title').a.get('href')
                user = cell.find('span', class_='topic_info').find_all('a')[1].text
                c_r = requests.get(url=c_url, headers={'user-agent': random.choice(self.headers)})
                soup = BeautifulSoup(c_r.text, 'lxml')
                content = soup.find('div', class_='topic_content')
                ctx = ''
                if content is not None:
                    if content.div is not None:
                        ctx = content.div.text
                    else:
                        ctx = content.text
                self.info.append({'user': user, 'title': title, 'context': ctx, 'tab': tab})


def create_sql(user, title, context='占位符', tab=' '):
    create_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return 'insert into v2ex(user, title, context, tab, create_time) values ({},{},{},{},{})' \
        .format(user, title, context, tab, create_time)


if __name__ == '__main__':
    d = downloader()
    db = Mysql()
    d.get_tabs()
    d.get_info()
    info = d.info
    for i in info:
        sql = create_sql(i['user'], i['title'], context=i['context'], tab=i['tab'])
        db.execute(sql)
