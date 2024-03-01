#!/usr/bin/python3
""" send request and display request id """


import urllib.request
import sys.argv

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
