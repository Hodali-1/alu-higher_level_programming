#!/bin/bash
# takes a URL, and displays the size in bytes of the response body
curl -s "$1" | wc -c
