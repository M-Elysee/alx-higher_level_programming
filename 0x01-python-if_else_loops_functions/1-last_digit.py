#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
if number < 0:
    last_d = last_d * -1
if last_d > 5:
    message = "and is greater than 5"
elif last_d == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_d} {message}")