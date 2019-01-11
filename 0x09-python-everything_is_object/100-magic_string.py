#!/usr/bin/python3
def magic_string(hbtn=[]):
    hbtn.insert(0, "Holberton, ")
    return ''.join(hbtn).rstrip(', ')
