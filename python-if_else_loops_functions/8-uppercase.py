#!/usr/bin/python3
def uppercase(str):
    """Print the string in uppercase, followed by a new line."""
    for c in str:
        print("{:c}".format(ord(c) - 32 if ord(c) >= 97 and ord(c) <= 122 else ord(c)), end="")
    print()
