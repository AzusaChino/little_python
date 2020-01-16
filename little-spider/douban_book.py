import random

import requests
from bs4 import BeautifulSoup

from common import headers


class Book:
    def __init__(self, isbn, name, author):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.rate = None
        self.pic = None
        self.publisher = None
        self.publish_date = None
        self.origin_name = None
        self.translator = None
        self.price = None
        self.page = None
        self.plurb = None


class Douban:

    def __init__(self):
        self.book_urls = []

    def get_urls(self, url=None):
        html = requests.get(url, headers={'user-agent': random.choice(headers)}).content
        soup = BeautifulSoup(html, 'lxml')
        book_list = soup.find('div', attrs={'class': 'article'}).find_all('table')
        next_page = soup.find('div', attrs={'class': 'paginator'}).find('span', attrs={'class': 'next'}).find('a').get(
            'href')
        for book in book_list:
            self.book_urls.append(book.find('div', attrs={'class': 'pl2'}).find("a").get("href"))
        while next_page:
            self.get_urls(next_page)

    def save(self, book: Book):
        pass


if __name__ == '__main__':
    d = Douban()
    d.get_urls('https://book.douban.com/top250')
    print(d.book_urls)
