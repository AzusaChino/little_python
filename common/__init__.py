import sqlite3
import pymongo
import pymysql

from pymongo.errors import PyMongoError
from pymysql import MySQLError
from sqlite3 import DatabaseError


class Mysql:

    def __init__(self, host='127.0.0.1', port=3306,
                 user='root', password='azusa520',
                 database='chino', charset='utf8mb4'):
        self.conn = pymysql.connect(host=host, port=port, user=user,
                                    password=password, database=database, charset=charset)
        self.cursor = self.conn.cursor()

    def query(self, sql, params=None):
        # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        # cursor.execute(sql, ('webmaster@python.org',))
        res = None
        try:
            self.cursor.execute(sql, params)
            res = self.cursor.fetchall()
        except MySQLError as e:
            print("发生了异常", e)
        return res

    def execute(self, sql, params=None):
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        with self.cursor as cur:
            cur.execute(sql, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


class Mongo:
    def __init__(self, host, port, dbname, collection):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[dbname]
        self.collection = self.db[collection]

    def save_data(self, data):
        try:
            self.collection.insert(data)
        except PyMongoError as e:
            print('发生了异常', e)
        print('保存成功!')

    def close(self):
        self.client.close()


class Sqlite:

    def __init__(self, location='./database.db'):
        self.conn = sqlite3.connect(location)
        self.cur = self.conn.cursor()

    def query(self, sql, params=None):
        res = None
        try:
            self.cur.execute(sql, params)
            res = self.cur.fetchall()
        except DatabaseError as e:
            print("error happened when query", e)
        return res

    def execute(self, sql, params=None):
        try:
            self.cur.execute(sql, params)
        except DatabaseError as e:
            print("error happened when execute", e)
            self.conn.rollback()
        self.conn.commit()
        print("execute succeed, sql: " + sql)

    def close(self):
        self.cur.close()
        self.conn.close()


headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 "
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 "
    "Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 "
    "Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
