def decorate(fn):
    def inner(name):
        print('Hello ' + fn(name))

    return inner


def _decorate(cb):
    def _(x, y):
        return cb(x, y)
    return _


@_decorate
def greet(name, a):
    return name + a


if __name__ == '__main__':
    print(greet('mick', 'a'))
