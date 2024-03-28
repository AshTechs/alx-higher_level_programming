#!/bin/bash
# Takes a URL as input, sends a request and displays the response in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
