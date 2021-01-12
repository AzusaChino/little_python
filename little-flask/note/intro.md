# virtualenv & flask

## usage of virtualenv

- create virtual env: virtualenv venv
- active: source venv/bin/active
- quit: deactive

## install flask

- before: pip freeze
- install: pip install flask
- after(check): pip freeze

## flask demo

```python
# coding:utf8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<div style='color:red'>Hello World</div>"

if __name__ == '__main__':
    app.run()

```
