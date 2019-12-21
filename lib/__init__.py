"""libraries of python-demo"""

def fib_seq(n):
    """Return a list of [F0...Fn]"""

    def fib_gen():
        """Fibonacci sequence generator. 0, 1, 1, 2, 3, 5, ..."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fg = fib_gen()
    return [next(fg) for _ in range(n + 1)]


def fib(n):
    """Returns the n-th number of fib"""
    a, b = 0, 1
    if n == 0:
        return a
    else:
        for _ in range(n):
            a, b = b, a + b
    return a


def fib_recursive(n):
    """Returns the n-th number of fib recursively"""
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp_memoize(n):
    """Returns the n-th number of fib with DP memoization"""
    memo = dict()
    def f(n):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return memo.setdefault(n, n)
        else:
            return memo.setdefault(n, f(n - 1) + f(n - 2))
    return f(n)

def fib_formula(n):
    sqrt_5 = 5**0.5
    return round(((1 + sqrt_5) / 2)**n / sqrt_5)
