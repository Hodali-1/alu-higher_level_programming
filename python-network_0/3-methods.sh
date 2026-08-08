#!/bin/bash
# takes a URL, and displays all HTTP methods the server accepts
curl -s -X OPTIONS "$1" -I | grep -i "Allow:" | cut -d " " -f 2- | tr -d "\r"
