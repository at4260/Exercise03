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
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2 

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calculate(user_input):
    while True:
        tokens = user_input.split()
        if tokens[0] == "+":
            return add(token[1], token[2])
        elif tokens[0] == "q":
            break


user_input = raw_input(">")
        
