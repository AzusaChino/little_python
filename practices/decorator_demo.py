def decorate(fn):
    def inner(name):
        print('Hello ' + fn(name))

    return inner


def _decorate(cb):
    def _(x, y):
        return x + y

    return _


@_decorate
def greet(name, a):
    return name


if __name__ == '__main__':
    print(greet('mick', 'a'))
