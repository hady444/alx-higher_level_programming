#!/usr/bin/python3
"""
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) <= 1:
        argument = ""
    else:
        argument = sys.argv[1]
    payload = {'q': argument}
    req = requests.post(url, data=payload)
    try:
        rsp = req.json()
        if rsp == {}:
            print("No result")
        else:
            print("[{}] {}".format(rsp.get("id"), rsp.get("name")))
    except ValueError:
        print("Not a valid JSON")
