#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    try:
        payload = {'q': letter}
        if not letter:
            payload = {'q': ""}
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)

