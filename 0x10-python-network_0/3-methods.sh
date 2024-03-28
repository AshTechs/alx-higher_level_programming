#!/bin/bash
# This script takes a URL as input and displays all HTTP.
curl -s -X OPTIONS -i "$1" | grep "Allow:" | cut -d ' ' -f 2-
