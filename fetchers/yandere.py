import os
import random
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.getcwd())

import fetchers


# Yandre Popular Fetcher
class YandereFetcher:
    base_url = "https://yande.re/post/"
    daily = "popular_by_day"
    weekly = "popular_by_week"
    monthly = "popular_by_month"

    def __init__(self, year="2022", month="09", folder=""):
        self.year = year
        self.month = month
        if folder != "":
            self.folder = "{}{}{}-{}".format(folder, os.sep, self.year, self.month)
        else:
            self.folder = "{}-{}".format(self.year, self.month)
        fetchers.create_dir_if_not_exists(self.folder)
        self.data_path = "{}{}{}".format(self.folder, os.sep, "data.csv")

    def download_by_daily(self):
        if not os.path.isfile(self.data_path):
            fd = open(self.data_path, "a+")
            for i in range(1, 32):
                url = "https://yande.re/post/popular_by_day?day={}&month={}&year={}".format(
                    i, self.month, self.year
                )
                cnt = 0
                while cnt < 10:
                    if self.save_metadata(url, fd):
                        break
                    else:
                        cnt += 1
            fd.close()
        self.do_download()

    def save_metadata(self, url, fd) -> bool:
        res = requests.get(url, headers={"user-agent": random.choice(fetchers.headers)})
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        # 找到所有的 show page
        popular = soup.find("ul", id="post-list-posts")
        if popular:
            images = popular.find_all("a", class_="thumb")
            # 依次访问热门图片
            for i in images:
                showid = str(i["href"]).removeprefix("/post/show/")
                fd.write(showid)
            return True
        else:
            print("当前页面 {} 尚无数据".format(url))
            return False

    def do_download(self):
        fd = open(self.data_path, "r")
        for i, si in fd.readlines():
            fetchers.download_by_showid(si)


if __name__ == "__main__":
    args = sys.argv[1:]
    year = "2022"
    month = "08"
    if len(args) == 1:
        month = args[0]
    if len(args) == 2:
        year = args[0]
        month = args[1]
    f = YandereFetcher(year, month, "E:{}Pictures{}{}".format(os.sep, os.sep, year))
    f.download_by_daily()
