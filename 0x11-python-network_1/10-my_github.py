#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == '__main__':
    url = f'https://api.github.com/users/{sys.argv[1]}'
    header = {'Authorization': f'token {sys.argv[2]}'}
    req = requests.get(url, headers=header)
    if req.status_code == 200:
        r = req.json()
        print(r.get('id'))
    else:
        print(None)
