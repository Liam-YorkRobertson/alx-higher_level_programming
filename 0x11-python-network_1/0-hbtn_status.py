#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        body = response.read()
        utf8 = body.decode("utf-8")

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf8)
