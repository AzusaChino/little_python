import random
import time

import requests
from openpyxl import Workbook

from common import Mysql


def get_json(url, page, lang):
    headers = {
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }
    data = {'first': 'false', 'pn': page, 'kd': lang}
    json = requests.post(url, data, headers=headers).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i.get('companyShortName', '无'))
        info.append(i.get('companyFullName', '无'))
        info.append(i.get('industryField', '无'))
        info.append(i.get('companySize', '无'))
        info.append(i.get('salary', '无'))
        info.append(i.get('city', '无'))
        info.append(i.get('education', '无'))
        info_list.append(info)
    return info_list


def save_wb(cities=None, lang='python'):
    wb = Workbook()
    db = Mysql()
    for c in cities:
        page = 1
        ws = wb.active
        ws.title = lang
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(c)
        while page < 31:
            info = get_json(url, page, lang)
            page += 1
            print(c, 'page', page)
            time.sleep(random.randint(10, 20))
            for row in info:
                sql = "INSERT INTO `python` (`shortname`, `fullname`, `industryfield`, `companySize`, `salary`, `city`, `education`) VALUES (%s, %s, %s, %s, %s, %s, %s)" % tuple(
                    row)
                db.execute(sql)
                ws.append(row)

    db.close()
    wb.save('{}职位信息.xlsx'.format(lang))
