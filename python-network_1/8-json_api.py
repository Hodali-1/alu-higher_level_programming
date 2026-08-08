#!/usr/bin/python3
"""Searches the search_user API and displays a matching user."""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
