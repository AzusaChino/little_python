import random
from tkinter import *

import requests
from bs4 import BeautifulSoup

from common import headers

res = requests.get("http://fanyi.baidu.com", headers={'user-agent': random.choice(headers)})
soup = BeautifulSoup(res.text, 'lxml')


class Interface:
    def __init__(self):
        self.root = Tk()

    def draw(self):
        self.root.title('~Translator~')
        self.root['width'] = 250
        self.root['height'] = 130
        Label(self.root, text="to translate: ", width=15).place(x=1, y=1)

        Entry(self.root, width=20).place(x=110, y=1)
        Label(self.root, text="translated result: ", width=18).place(x=1, y=20)
        s = StringVar().set("Welcome, this is a test")
        Entry(self.root, width=20, textvariable=s).place(x=110, y=20)
        btn1 = Button(self.root, text="DO", width=8).place(x=40, y=80)
        btn2 = Button(self.root, text="CLEAR", width=8).place(x=110, y=80)
        btn1.bind()
