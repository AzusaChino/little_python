import sqlite3

books = [{"021", 25, "CS"}, {"022", 30, "ENGLISH"}, {"023", 18, "ART"}, {"024", 35, "MUSIC"}]


class db:
    def __init__(self):
        self.conn = None
        self.cur = None

    def select(self, sql, param=None):
        self.conn = sqlite3.connect('./sales.db')
        self.cur = self.conn.cursor()
        res = None
        try:
            if param is not None:
                self.cur.execute(sql, param)
            else:
                self.cur.execute(sql)
            res = self.cur.fetchall()
        except Exception:
            print("error occurred")
        self.cur.close()
        self.conn.close()
        return res

    def query(self, sql, param=None):
        self.conn = sqlite3.connect('./sales.db')
        self.cur = self.conn.cursor()
        try:
            if param is not None:
                self.cur.execute(sql, param)
            else:
                self.cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            print("error, rollback complete")
        self.cur.close()
        self.conn.close()
        print("query success: " + sql)


if __name__ == '__main__':
    db = db()
    print(db.select("select * from book"))
