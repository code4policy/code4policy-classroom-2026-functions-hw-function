def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def square_n_times(number, n):
    """
    Squares `number` n times, summing each intermediate squared value.

    Example: number=2, n=3
      2^2 = 4
      4^2 = 16
      16^2 = 256
      return 4 + 16 + 256 = 276
    """
    total = 0
    value = number
    for _ in range(n):
        value = value ** 2
        total += value
    return total
