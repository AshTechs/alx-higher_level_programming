#!/bin/bash
# This script takes a URL as input, sends a request to it, and displays
# the size of the body of the response in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
