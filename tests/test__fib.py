from lib import fib

def test__fib_seq():
    assert fib.seq(0) == [0]
    assert fib.seq(2) == [0, 1, 1]
    assert fib.seq(7) == [0, 1, 1, 2, 3, 5, 8, 13]

def test__fib_iterative():
    assert fib.iterative(0) == 0
    assert fib.iterative(1) == 1
    assert fib.iterative(30) == 832040

def test__fib_recursive():
    assert fib.recursive(0) == 0
    assert fib.recursive(1) == 1
    assert fib.recursive(30) == 832040

def test__fib_dp_memoize():
    assert fib.dp(0) == 0
    assert fib.dp(1) == 1
    assert fib.dp(30) == 832040

def test__fib_formula():
    assert fib.formula(0) == 0
    assert fib.formula(1) == 1
    assert fib.formula(30) == 832040
