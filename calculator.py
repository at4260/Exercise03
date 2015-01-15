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

from arithmetic import *
def main():
    while True:
        user_input = raw_input(">Enter equation")
        token = user_input.split()
        if token[0] == "+":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print add(a, b)
        elif token[0] == "-":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print subtract(a, b)
        elif token[0] == "*":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print multiply(a, b)
        elif token[0] == "/":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print divide(a, b)
        elif token[0] == "square":
            a_str = token[1]
            a = int(a_str)
            print square(a)
        elif token[0] == "cube":
            a_str = token[1]
            a = int(a_str)
            print cube(a)
        elif token[0] == "pow":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print power(a, b)
        elif token[0] == "mod":
            a_str = token[1]
            b_str = token[2]
            a = int(a_str)
            b = int(b_str)
            print mod(a, b)
        elif token[0] == "q":
            break
        else:
            print "I don't understand"

if __name__ == '__main__':
    main()
