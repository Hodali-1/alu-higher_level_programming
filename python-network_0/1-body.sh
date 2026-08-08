#!/bin/bash
# takes a URL, follows redirects, and displays the body only for a 200
curl -s -f -L "$1"
