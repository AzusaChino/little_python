import random
import re
import sqlite3
from collections import deque

import requests
from bs4 import BeautifulSoup

from common import headers


class db:
    conn = None
    cur = None

    def __init__(self):
        self.conn = sqlite3.connect('./database.db')
        self.cur = self.conn.cursor()

    def query(self, sql, params=None):
        res = None
        try:
            self.cur.execute(sql, params)
            res = self.cur.fetchall()
        except:
            print("error happened when query")
        return res

    def execute(self, sql, params=None):
        try:
            self.cur.execute(sql, params)
        except:
            print("error happened when execute")
            self.conn.rollback()
        self.conn.commit()
        print("execute succeed, sql: " + sql)

    def close(self):
        self.cur.close()
        self.conn.close()


class spider:
    base_url = 'https://www.ustc.edu.cn/'
    un_visited = deque()
    visited = set()
    count = 0

    def __init__(self):
        pass

    def fetch_urls(self):
        res = None
        try:
            res = requests.get(self.base_url, headers={'user-agent': random.choice(headers)})
            res.encoding = 'utf-8'
        except:
            print("error when requests.get()")
        soup = BeautifulSoup(res.text, 'lxml')
        news_div = soup.find('div', id='wp_news_w1')
        a_s = news_div.find_all('a')
        for a in a_s:
            u = a.get('href')
            if reg(u):
                if (u not in self.un_visited) and (u not in self.visited):
                    self.un_visited.append(u)
        print(self.un_visited)

    def download(self):
        while self.un_visited:
            url = self.un_visited.popleft()
            self.visited.add(url)
            self.count += 1
            try:
                res = requests.get(url, headers={'user-agent': random.choice(headers)})
                res.encoding = 'utf-8'
            except:
                print("error when requests.get()")


def reg(url):
    if re.match(r'http.+', url):
        if not re.match(r'http[s]?://news\.ustc\.edu\.cn', url):
            return False
        else:
            return True


if __name__ == '__main__':
    s = spider()
    s.fetch_urls()
