#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
and displays the body of the response.
If an error is returned, the error code should be
printed.
"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(data.decode('utf-8'))
