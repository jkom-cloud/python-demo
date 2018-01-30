import lib

def test__fib_gen():
    assert lib.fib_seq(0) == [0]
    assert lib.fib_seq(2) == [0, 1, 1]
    assert lib.fib_seq(7) == [0, 1, 1, 2, 3, 5, 8, 13]
