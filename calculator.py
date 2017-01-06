"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    input_string = raw_input()
    tokens = input_string.split(" ")

    if len(tokens) < 3 and tokens[0] == "+":
        print "I can't make any operation with just a number"
    elif len(tokens) == 3 and tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "+":
        print add_from_list(tokens)

    elif len(tokens) < 3 and tokens[0] == "-":
        print "I can't make any operation with just a number"
    elif len(tokens) == 3 and tokens[0] == "-":
        print subtract(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "-":
        print subtrac_from_list(tokens)

    elif len(tokens) < 3 and tokens[0] == "*":
        print "I can't make any operation with just a number"
    elif len(tokens) == 3 and tokens[0] == "*":
        print multiply(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "*":
        print multiply_from_list(tokens)

    elif len(tokens) < 3 and tokens[0] == "/":
        print "I can't make any operation with just a number"
    elif len(tokens) == 3 and tokens[0] == '/':
        print divide(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "/":
        print "I can't make this operation with more that two numbers"

    elif len(tokens) == 1 and tokens[0] == "square":
        print "I can't make this operation without a number"
    elif len(tokens) < 3 and tokens[0] == "square":
        print square(int(tokens[1]))
    elif len(tokens) >= 3 and tokens[0] == 'square':
        print "I can't make this operation with more that two numbers"
    
    elif len(tokens) == 1 and tokens[0] == "cube":
        print "I can't make this operation without a number"
    elif len(tokens) < 3 and tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif len(tokens) >= 3 and tokens[0] == 'cube':
        print "I can't make this operation with more that two numbers"

    elif len(tokens) < 3 and tokens[0] == "power":
        print "I can't make this operation without a number"
    elif len(tokens) == 3 and tokens[0] == 'power':
        print power(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "power":
        print "I can't make this operation with more that two numbers"

    elif len(tokens) < 3 and tokens[0] == "mod":
        print "I can't make this operation without a number"
    elif len(tokens) == 3 and tokens[0] == 'mod':
        print mod(int(tokens[1]), int(tokens[2]))
    elif len(tokens) > 3 and tokens[0] == "mod":
        print "I can't make this operation with more that two numbers"

    else:
        print "I dont understand"


