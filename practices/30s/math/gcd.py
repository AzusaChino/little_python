"""
math.gcd works with only two numbers

Calculates the greatest common divisor between two or more numbers/lists.

The helperGcdfunction uses recursion. Base case is when y equals 0. In this case, return x. Otherwise, return the GCD of y and the remainder of the division x/y.

Uses the reduce function from the inbuilt module functools. Also defines a method spread for javascript like spreading of lists.
"""

from functools import reduce


def spread(arg):
    result = []
    for i in arg:
        if isinstance(i, list):
            result.extend(i)
        else:
            result.append(i)
    return result


def gcd(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else gcd(y, x % y)

    return reduce((lambda x, y: _gcd(x, y)), numbers)


if __name__ == '__main__':
    print(gcd(8, 30))
