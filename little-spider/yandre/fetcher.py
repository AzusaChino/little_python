import os
import random
import time

import requests
from bs4 import BeautifulSoup

headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
    "Opera/9.25 (Windows NT 5.1; U; en)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12",
    "Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
]

# Yandre Popular Fetcher
class Fetcher(object):
    base_url = "https://yande.re/post/"
    daily = "popular_by_day"
    weekly = "popular_by_week"
    monthly = "popular_by_month"

    def __init__(self, year=2022, month=8, folder=""):
        self.year = year
        self.month = month
        if folder != "":
            self.folder = "{}{}{}-{}".format(folder, os.sep, self.year, self.month)
        else:
            self.folder = "{}-{}".format(self.year, self.month)

    def download_by_daily(self):
        create_dir(self.folder)
        # TODO fix daily range
        for i in range(1, 27):
            url = "https://yande.re/post/popular_by_day?day={}&month={}&year={}".format(
                i, self.month, self.year
            )
            self.do_download(url)

    def do_download(self, url):
        """
        真正下载的方法
        """
        res = requests.get(url, headers={"user-agent": random.choice(headers)})
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        # 找到所有的 show page
        popular = soup.find("ul", id="post-list-posts")
        images = popular.find_all("a", class_="thumb")

        # 依次访问热门图片
        for i in images:
            fi = str(i["href"]).removeprefix("/post/show/")
            self.download_by_showid(fi)
            time.sleep(1)

    def download_by_showid(self, fi):
        """
        fi: show id
        """
        jpg_name = "{}/{}.jpg".format(self.folder, fi)
        png_name = "{}/{}.png".format(self.folder, fi)
        if os.path.exists(jpg_name) or os.path.exists(png_name):
            print("{} 已存在".format(fi))
            return

        u = "https://yande.re/post/show/{}".format(fi)
        pr = requests.get(u, headers={"user-agent": random.choice(headers)})
        pr.encoding = "utf-8"
        sp = BeautifulSoup(pr.text, "html.parser")

        png = sp.find("a", id="png")
        jpg = sp.find("a", id="highres")

        # 尝试下载PNG
        if png:
            pd = requests.get(
                str(png["href"]), headers={"user-agent": random.choice(headers)}
            )
            with open(png_name, "wb") as f:
                f.write(pd.content)
            print("{}.png 下载完成".format(fi))
        # 下载 JPG
        elif jpg:
            pd = requests.get(
                str(jpg["href"]), headers={"user-agent": random.choice(headers)}
            )
            with open(jpg_name, "wb") as f:
                f.write(pd.content)
            print("{}.jpg 下载完成".format(fi))
        else:
            print("{} 未找到下载地址".format(fi))


def create_dir(dir_name) -> None:
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


if __name__ == "__main__":
    f = Fetcher(2022, 8, "E:\\Pictures\\2022")
    f.download_by_showid(1013676)
