import sqlite3


class Db:
    conn = None
    cur = None

    def __init__(self):
        self.conn = sqlite3.connect('./flask.db')
        self.cur = self.conn.cursor()

    def query(self, sql, params=None):
        res = None
        try:
            self.cur.execute(sql, params)
            res = self.cur.fetchall()
        except:
            print("error happened when query")
        return res

    def execute(self, sql, params=None):
        try:
            self.cur.execute(sql, params)
        except:
            print("error happened when execute")
            self.conn.rollback()
        self.conn.commit()
        print("execute succeed, sql: " + sql)

    def close(self):
        self.cur.close()
        self.conn.close()
