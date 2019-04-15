#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as hbtn:
        status = hbtn.read()
    print("Body response:")
    print("\t- type: {}\n\t- content: {}\n\t- utf-8 content: {}"
          .format(type(status), status, status.decode('utf-8')))
