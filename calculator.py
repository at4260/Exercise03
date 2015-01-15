"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

Pseudocode for REPL:

# No setup
repeat forever:
    read input
    tokenize input
    if the first token is 'q', quit
    otherwise decide which math function to call based on the tokens we read
"""

# def main():
#     pass


# if __name__ == '__main__':
#     main()
from arithmetic import *

def calculate(user_input):
    while True:
        token = user_input.split()
        a_str = token[1]
        b_str = token[2]
        a = int(a_str)
        b = int(b_str)
        if token[0] == "+":
            print add(a, b)
            break
        elif token[0] == "-":
            return subtract(a, b)
        elif token[0] == "*":
            return multiply(a, b)
        elif token[0] == "q":
            break

# def divide(num1, num2):
#     return num1 / num2 

# def square(num1):
#     return num1 ** 2

# def cube(num1):
#     return num1 ** 3

# def power(num1, num2):
#     return num1 ** num2

# def mod(num1, num2):
#     return num1 % num2

user_input = raw_input(">Enter equation")
calculate(user_input)
        
