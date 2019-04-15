#!/usr/bin/python3
"""
Takes Github username and password and uses
the Github API to display id
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url, data={'username': sys.argv[1],
                                'password': sys.argv[2]})
    r = dict(r.json())
    print(r)
    print(r.get('id'))
