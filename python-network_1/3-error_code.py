#!/usr/bin/python3
"""Fetches a URL and prints the body, or the HTTP error code."""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
