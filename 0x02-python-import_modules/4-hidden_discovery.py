#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    test = dir(hidden_4)
    index = 0
    for index, name in enumerate(test):
        if name[0:2] != '__':
            print('{}'.format(test[index]))
