"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    input_string = raw_input()
    token = input_string.split(" ")
    if token[0] == 'q':
        break
    elif token[0] == "+":
        print add(int(token[1]), int(token[2])) 

    elif token[0] == '-':
        print subtract(int(token[1]), int(token[2]))
    elif token[0] == '*':
        print multiply(int(token[1]), int(token[2]))
    elif token[0] == '/':
        print divide(int(token[1]), int(token[2]))
    elif token[0] == 'square':
        print square(int(token[1]))
    elif token[0] == 'cube':
        print cube(int(token[1]))
    elif token[0] == 'power':
        print power(int(token[1]), int(token[2]))
    elif token[0] == 'mod':
        print mod(int(token[1]), int(token[2]))
    else:
        print "I dont understand"


