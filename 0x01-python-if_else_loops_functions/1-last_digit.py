#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
put = "Last digit of {} is {} and is "
if last > 5:
    print(put.format(number, last) + "greater than 5")
elif last == 0:
    print(put.format(number, last) + "0")
else:
    print(put.format(number, last) + "less than 6 and not 0")
