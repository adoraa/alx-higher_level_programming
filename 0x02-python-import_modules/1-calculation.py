#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    sumres = add(a, b)
    difres = sub(a, b)
    prdres = mul(a, b)
    divres = div(a, b)
    print("{} + {} = {}".format(a, b, sumres))
    print("{} - {} = {}".format(a, b, difres))
    print("{} * {} = {}".format(a, b, prdres))
    print("{} / {} = {}".format(a, b, divres))
