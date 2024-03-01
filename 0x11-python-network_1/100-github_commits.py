#!/usr/bin/python3
"""
    script that takes 2 arguments in order to solve this challenge
"""


import requests
import sys

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    req = requests.get(url)
    if req.status_code == 200:
        r = req.json()
        for commit in r[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    else:
        # If the request was not successful, print an error message
        print("Error:", req.status_code)
