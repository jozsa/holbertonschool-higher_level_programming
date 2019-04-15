#!/usr/bin/python3
"""
Sends a search request to Star Wars API
and displays results.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    r = dict(r.json())
    print('Number of results: {}'.format(len(r.get('results'))))
    for k in r.get('results'):
        print(k.get('name'))
