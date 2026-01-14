def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def square(x):
    return x * x


def cube(x):
    return x ** 3


def square_n_times(number, n):
        result = number 
        for _ in range(n):
            result = square(result)
        return result

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)   

