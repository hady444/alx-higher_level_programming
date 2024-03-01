#!/usr/bin/python3
""" simple request for URL """


import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    content = req.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", req.text)
