import os
import random
import sys

import requests
from bs4 import BeautifulSoup

# 将当前文件夹加入到 py 环境变量
sys.path.append(os.getcwd())

import fetchers


# Konachan Popular Fetcher
class KonachanFetcher:
    base_url = "https://konachan.com/post/"

    def __init__(self, year="2022", month="08", folder=""):
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
                url = self.base_url + "popular_by_day?day={}&month={}&year={}".format(
                    i, self.month, self.year
                )
                cnt = 0
                while cnt < 10:
                    if self.save_metadata(url, fd):
                        break
                    else:
                        cnt += 1
            fd.close()
            print("完成 showId 采集")
        self.do_download(self.folder)

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
                # sample: https://konachan.com/post/show/347142/aqua_eyes-ass-breasts-chinese_clothes-chinese_dres
                showid = str(i["href"]).split("/")[3]
                fd.write("{}\n".format(showid))
            return True
        else:
            print("当前页面 {} 尚无数据".format(url))
            return False

    def do_download(self, folder):
        fd = open(self.data_path, "r")
        for si in fd.readlines():
            # clean right `\n`
            fetchers.download_by_showid(si.rstrip(), folder, self.base_url + "show/{}")
        fd.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    # default param
    year = "2022"
    month = "08"
    # extract target year & month from args
    if len(args) == 1:
        month = args[0]
    if len(args) == 2:
        year = args[0]
        month = args[1]
    target_folder = "E:{}Pictures{}{}{}konachan".format(os.sep, os.sep, year, os.sep)
    kf = KonachanFetcher(year, month, target_folder)
    kf.download_by_daily()
