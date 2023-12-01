#!/usr/bin/python3
"""
    Script that fetches https://alx-intranet.hbtn.io/status and displays the body of the response.
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        print(f"\t- type: {type(response.content)}")
        print(f"\t- content: {response.content.decode('utf-8')}")
    else:
        print("Failed to fetch")
