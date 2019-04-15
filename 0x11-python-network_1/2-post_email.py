#!/usr/bin/python3
"""
Script that takes in an URL and an email,
sends a POST request to the passed URL using
the email, and displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
