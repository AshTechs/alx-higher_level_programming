#!/bin/bash
# Takes a URL, sends a GET request, and displays the response.
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
