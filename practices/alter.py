import pymysql


class Mysql:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.11.8', port=3306, user='root',
                                    password='abcd1234', db='KSSK_DLUO', charset='utf8mb4')
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        with self.cursor as cur:
            cur.execute(sql, params)
        self.conn.commit()

    def query(self, sql, params=None):
        res = None
        try:
            self.cursor.execute(sql, params)
            res = self.cursor.fetchall()
        except Exception:
            print("error occurred when query, sql : " + sql)
        return res

    def close(self):
        self.cursor.close()
        self.conn.close()


class App:
    def __init__(self):
        self.db = Mysql()


if __name__ == '__main__':
    app = App()
