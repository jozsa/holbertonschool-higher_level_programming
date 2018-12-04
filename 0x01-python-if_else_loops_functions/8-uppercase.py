#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 123 > ord(letter) > 96:
            letter = chr(ord(letter) - 32)
        print('{}'.format(letter), end="")
    print('')
