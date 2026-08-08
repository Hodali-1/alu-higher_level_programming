#!/usr/bin/python3
"""Displays the X-Request-Id header value for a given URL, via requests."""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
