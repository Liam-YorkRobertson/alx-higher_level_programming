#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    try:
        response = requests.post(url, data)
        usr_info = response.json()
        if usr_info:
            print(f"[{usr_info['id']}] {usr_info['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
