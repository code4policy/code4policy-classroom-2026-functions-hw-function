def multiply(a,b):
    return a * b

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def divide(a,b):
	return a/b

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

def square(x):
    """Return x squared."""
    return x ** 2


def cube(x):
    """Return x cubed."""
    return x ** 3

def square_n_times(number, n):
    """Square the number n times and return the sum."""
    total = 0
    current = number

    for _ in range(n):
        current = current ** 2
        total += current

    return total

