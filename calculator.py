def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
    return a * b

def divide(a,b):
	return a/b

def square(a):
	return a*a

def cube(a):
	return a*a*a

def square_n_times(number, n):
	if n < 0:
		raise ValueError("n must be non-negative number")
	total = 0
	value = number
	for _ in range(n):
		value = value * value
		total += value
	return total

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)