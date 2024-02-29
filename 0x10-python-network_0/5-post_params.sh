#!/bin/bash
# takes in a URL, sends a POST request URL, and displays the body
curl -sX Post -d "'email': 'test@gmail.com', 'subject': 'I will always be here for PLD'" $1
