#!/usr/bin/python3
"""
     Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            return request_id
        else:
            return "X-Request-Id not found in headers"
    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 5-hbtn-header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
