"""Fibonacci Numbers"""


def seq(n):
    """Return a list of [F0...Fn]"""

    def fib_gen():
        """Fibonacci sequence generator. 0, 1, 1, 2, 3, 5, ..."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fg = fib_gen()
    return [next(fg) for _ in range(n + 1)]


def iterative(n):
    """Returns the n-th number of fib"""
    a, b = 0, 1
    if n == 0:
        return a
    else:
        for _ in range(n):
            a, b = b, a + b
    return a


def recursive(n):
    """Returns the n-th number of fib recursively"""
    if n == 0 or n == 1:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)


def dp(n):
    """Returns the n-th number of fib with DP"""
    f = [0] * (n + 1)
    for i in range(n + 1):
        if i <= 1:
            f[i] = i
        else:
            f[i] = f[i - 1] + f[i - 2]
    return f[n]


def formula(n):
    """Returns the n-th number of fib with math formula"""
    sqrt_5 = 5**0.5
    return round(((1 + sqrt_5) / 2)**n / sqrt_5)
