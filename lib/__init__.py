"""libraries of python-demo"""

def fib_gen():
    """Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_seq(n):
    """return a sequence of F0...Fn"""
    fg = fib_gen()
    return [next(fg) for i in range(n + 1)]
