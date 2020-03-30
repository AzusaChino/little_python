import requests
from bs4 import BeautifulSoup
import json
from common import Mongo


#  思路分析 和 伪代码(汉字 开发思路)
#  1.查找入口 分析 url https://bj.lianjia.com/
#  2.准确的url : https://bj.lianjia.com/ershoufang/rs%E4%B8%9C%E5%9F%8E%E5%8C%BA/


class Lianjia_Spider:
    #  2.python 代码 实现发送请求
    def __init__(self):
        self.place = input('请输入想抓取的地区:')

        self.base_url = 'https://bj.lianjia.com/ershoufang/rs' + self.place
        # 最大的数据集合
        self.data_list = []

    def get_data(self):
        #  不同页面 应该有不同的 url
        data = requests.get(self.base_url).content.decode('utf-8')

        return data

    #  3.接收返回的数据  解析
    def parse_data(self, data):
        # 3.1 将 爬虫获取的数据 解析类型转换
        soup = BeautifulSoup(data, 'lxml')

        # 3.2 根据css选择器 提取数据验证 列表数组
        #  1.解析出数据列表
        data_list = soup.select('.sellListContent li')

        #  遍历 每一个条数据 提取详细信息
        for li in data_list:

            # 用字典 标识数据 key:Value
            dict_data = {}

            #  1.房屋标题
            #  li -- > a --> img --->alt
            if len(li.select('a img')) > 0:
                dict_data['room_name'] = li.select('a img')[0].get('alt')

            # 2. 房屋信息
            if len(li.select('.houseInfo')) > 0:
                dict_data['content'] = li.select('.houseInfo')[0].get_text()

            # 3. 价格
            if len(li.select('.totalPrice')) > 0:
                dict_data['price'] = li.select('.totalPrice')[0].get_text()

            # 将所有的 dict 数据 再次放入一个 大篮子里面
            self.data_list.append(dict_data)

    # 4.保存数据 本地文件
    def save_data_file(self):
        # 首先保存到 本地文件查看 看是否是静态数据页面
        #  写入本地文件 必须是字符串类型 所以我们需要转换类型
        data_str = json.dumps(self.data_list)
        with open('data.json', 'w') as f:
            f.write(data_str)
            print('数据保存成功!')

    # 5. 保存到 mongo数据库里面
    def save_mongo_base(self):
        # 1.有数据库
        data_base = Mongo('127.0.0.1', 27017, 'Lianjia', 'room')

        # 2. 保存
        data_base.save_data(self.data_list)

        print('保存成功!')

    # 6.开启爬虫
    def start(self):

        data = self.get_data()

        # 2. 解析数据
        self.parse_data(data)

        # 3. 保存数据 文件
        # spider.save_data_file()

        # 4. 保存数据库
        self.save_mongo_base()


if __name__ == '__main__':
    Lianjia_Spider().start()
