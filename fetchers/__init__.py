import os
import random

import requests
from bs4 import BeautifulSoup

headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36",
]


def create_dir_if_not_exists(dir_name) -> None:
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def download_by_showid(showid: str, folder: str, base_url: str):
    """
    根据 showid 进行下载
    showid: show id
    folder: 目标路径
    base_url: show地址
    """
    jpg_name = "{}/{}.jpg".format(folder, showid)
    png_name = "{}/{}.png".format(folder, showid)
    if os.path.exists(jpg_name) or os.path.exists(png_name):
        print("{} 已存在".format(showid))
        return

    u = base_url.format(showid)
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
        print("{}.png 下载完成".format(showid))
    # 下载 JPG
    elif jpg:
        pd = requests.get(
            str(jpg["href"]), headers={"user-agent": random.choice(headers)}
        )
        with open(jpg_name, "wb") as f:
            f.write(pd.content)
        print("{}.jpg 下载完成".format(showid))
    else:
        print("{} 未找到下载地址".format(showid))
