def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def square(a):
	return a * a

def cube(a):
	return a * a * a

def square_n_times(number, n):
	updated_number = 0
	changed_number = number
	for times in range(n):
		changed_number = changed_number * changed_number
		updated_number = updated_number + changed_number
	return updated_number

print("I'm going use the calculator functions to divide 30 by 6")
x = divide(30,6)
print(x) 

# print("I'm going use the calculator functions to raise 30 by the power of 2")
# x = square(30)
# print(x) 

# print("I'm going use the calculator functions to determine 30 cubed")
# x = cube(30)
# print(x) 

# print("I'm going use the calculator functions to determine 3 cubed")
# x = square_n_times(3, 3)
# print(x) 