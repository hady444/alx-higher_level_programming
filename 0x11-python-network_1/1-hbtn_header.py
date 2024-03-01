#!/usr/bin/python3
""" send request and display request id """


import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    #req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get('X-Request-Id'))
