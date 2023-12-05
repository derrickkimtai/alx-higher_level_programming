#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and displays the body of the response.
"""
import sys
import requests

def fetch_response(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    fetch_response(url)
