from calculator import add, subtract, multiply, divide, square, cube, square_n_times


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(8, 2) == 4


def test_square():
    assert square(5) == 25


def test_cube():
    assert cube(3) == 27


def test_square_n_times():
    assert square_n_times(2, 3) == 276
    assert square_n_times(10, 0) == 0
