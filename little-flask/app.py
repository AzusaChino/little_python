import src

app = src.create_app()

if __name__ == '__main__':
    app.run('localhost', '9090')
