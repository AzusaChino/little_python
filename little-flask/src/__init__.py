import os
import random

from db import Sqlite3
from flask import Flask


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'test.sqlite')
    )
    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'hello.html'

    @app.route('/create', methods=["POST"])
    def create(body):
        sql_lite = Sqlite3()
        sql_lite.execute("create table test(id int auto_increment, value varchar(100))")
        sql_lite.execute("insert into test values(%d, %s)".format(random.randint, body))
        return 'execute success'

    return app
