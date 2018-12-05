#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
print('Last digit of {:d} is {:d} '.format(number, lastdigit), end="")
if lastdigit == 0:
    print('and is 0')
elif lastdigit < 6:
    print('and is less than 6 and not 0')
elif lastdigit > 5:
    print('and is greater than 5')
