#!/usr/bin/python3
""" send request and display request id """


import urllib.request
from sys import argv

url = argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
