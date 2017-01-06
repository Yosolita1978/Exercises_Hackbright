def add(num1, num2):
    """Return the sum of two numbers"""
    return num1 + num2

def add_from_list(input_list):
    sum_num = int(input_list[1])
    for number in range(2, len(input_list)):
        sum_num = sum_num + int(input_list[number])
    return sum_num


def subtract(num1, num2):
    """Return the difference of two numbers"""
    return num1 - num2

def subtrac_from_list(input_list):
    sub_num = int(input_list[1])
    for number in range(2, len(input_list)):
        sub_num = sub_num - int(input_list[number])
    return sub_num


def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2

def multiply_from_list(input_list):
    multiply_num = int(input_list[1])
    for number in range(2, len(input_list)):
        multiply_num = multiply_num * int(input_list[number])
    return multiply_num


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / num2


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return num * num * num


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
