from common import Sqlite

books = [{"021", 25, "CS"}, {"022", 30, "ENGLISH"}, {"023", 18, "ART"}, {"024", 35, "MUSIC"}]

if __name__ == '__main__':
    db = Sqlite('./sales.db')
    print(db.query("select * from book"))
