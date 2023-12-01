#!/usr/bin/python3
import sys
import urllib.request
# script that takes in a URL, sends a request to the URL

url = sys.argv[1]

with urllib.request.urlopen(url, timeout=10) as response:
    request_id = response.headers['X-Request-Id']
    print(request_id)
