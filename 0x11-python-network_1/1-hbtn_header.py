#!/usr/bin/python3
"""
Send request to URL passed as 1st argument to program
and display the value of the 'X-Request-Id' variable of that URL
"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    response = urllib.request.urlopen(req)
    print(response.info().get('X-Request-Id'))
