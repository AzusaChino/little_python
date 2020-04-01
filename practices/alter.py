from common import Mysql


class App:
    def __init__(self):
        self.db = Mysql(host='192.168.11.8', port=3306, user='root',
                        password='abcd1234', db='KSSK_DLUO', charset='utf8mb4')


if __name__ == '__main__':
    app = App()
