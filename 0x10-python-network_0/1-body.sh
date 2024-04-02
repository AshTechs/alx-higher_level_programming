#!/bin/bash
# This script takes a URL as input, sends a GET request to it, and displays the body of the response for a 200 status code with one redirection and for other status codes with five redirections
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1" || curl -s -o /dev/null -w "%{http_code}" "$1" 2>&1 >/dev/null | grep -qE '30[0-9]|404|50[0-9]'
