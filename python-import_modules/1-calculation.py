#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5

if __name__ == "__main__":
    print('Addition result: {}'.format(add(a, b)))
    print('Subtraction result: {}'.format(sub(a, b)))
    print('Multiplication result: {}'.format(mul(a, b)))
    print('Division result: {}'.format(div(a, b)))
