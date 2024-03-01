#!/usr/bin/python3
""" send request and display request id """


import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
