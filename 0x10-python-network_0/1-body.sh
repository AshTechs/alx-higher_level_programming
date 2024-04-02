#!/bin/bash
# This script takes a URL as input, sends a GET request to it, and displays the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
