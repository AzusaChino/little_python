from functools import wraps


def memorization(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memorization
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(5))


class myDecorator(object):
    def __init__(self, fn):
        print("inside myDecorator.__init__()")
        self.fn = fn

    def __call__(self):
        self.fn()
        print("inside myDecorator.__call__()")


@myDecorator
def aFunction():
    print("inside aFunction()")


print("Finished decorating aFunction()")

aFunction()
