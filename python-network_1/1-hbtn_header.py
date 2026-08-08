#!/usr/bin/python3
"""Displays the X-Request-Id header value for a given URL, via urllib."""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.getheader("X-Request-Id"))
