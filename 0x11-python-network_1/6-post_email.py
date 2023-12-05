#!/usr/bin/python3
"""
    takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys

def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        return response.text
    except requests.RequestException as e:
        return f"Request failed: {e}"
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit[1]

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
