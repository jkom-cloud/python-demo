import lib

def test__fib_gen():
    assert lib.fib_seq(0) == [0]
    assert lib.fib_seq(2) == [0, 1, 1]
    assert lib.fib_seq(7) == [0, 1, 1, 2, 3, 5, 8, 13]

def test__fib():
    assert lib.fib(0) == 0
    assert lib.fib(1) == 1
    assert lib.fib(30) == 832040

def test__fib_recursive():
    assert lib.fib_recursive(0) == 0
    assert lib.fib_recursive(1) == 1
    assert lib.fib_recursive(30) == 832040

def test__fib_dp_memoize():
    assert lib.fib_dp_memoize(0) == 0
    assert lib.fib_dp_memoize(1) == 1
    assert lib.fib_dp_memoize(30) == 832040

def test__fib_formula():
    assert lib.fib_formula(0) == 0
    assert lib.fib_formula(1) == 1
    assert lib.fib_formula(30) == 832040
