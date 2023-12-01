#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL
"""
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url, timeout=10) as response:
        request_id = response.headers.get('X-Request-Id')
        print(dict(request_id))
