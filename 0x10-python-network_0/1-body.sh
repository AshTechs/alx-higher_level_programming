#!/bin/bash
# Takes a URL, sends a GET request, and displays the response.
url="$1"; curl -s -w '%{http_code}' "$url" -o temp.txt ; [ $(tail -n1 temp.txt) -eq 200 ] && cat temp.txt ; rm temp.txt
