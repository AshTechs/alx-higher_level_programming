#!/bin/bash
# Takes a URL, sends a POST request, and displays the response.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
