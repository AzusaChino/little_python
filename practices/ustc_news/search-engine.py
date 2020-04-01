import random
import re
from collections import deque

import requests
from bs4 import BeautifulSoup

from common import headers, Sqlite


class spider:
    base_url = 'https://www.ustc.edu.cn/'
    un_visited = deque()
    visited = set()
    count = 0

    def __init__(self):
        self.db = Sqlite()

    def fetch_urls(self):
        res = None
        try:
            res = requests.get(self.base_url, headers={'user-agent': random.choice(headers)})
            res.encoding = 'utf-8'
        except Exception as e:
            print("error when requests.get()", e)
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
            except Exception as e:
                print("error when requests.get()", e)


def reg(url):
    if re.match(r'http.+', url):
        if not re.match(r'http[s]?://news\.ustc\.edu\.cn', url):
            return False
        else:
            return True


if __name__ == '__main__':
    s = spider()
    s.fetch_urls()
