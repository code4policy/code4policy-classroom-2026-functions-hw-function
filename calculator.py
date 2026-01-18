def multiply(a, b):
	return a * b


def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def divide(a, b):
	return a / b

def square(a):
	return a * a

def cube(a):
	return a * a * a

def square_n_times (number, n):
	for _ in range(n):
		number = number ** 2
	return number	


print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5, 6)
print(x)