#!/usr/bin/python3
"""
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if argv[1]:
        q = argv[1]
    payload = {'q': q}
    req = requests.post(url, data=payload)
    r = req.json()
    try:
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError as e:
        print("Not a valid JSON")
