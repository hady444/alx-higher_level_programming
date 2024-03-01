#!/usr/bin/python3
""" input: url, email
    send post request with params
    display body of response
"""


import urllib.request
import urllib.parse
import sys.argv
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print("your email is:", response.read().decode('utf-8'))
