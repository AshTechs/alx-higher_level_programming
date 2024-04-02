#!/bin/bash
# This script sends a GET request to a specified URL and displays the body of the response if the status code is 200
curl -s -o /dev/null -w "%{http_code}" $1 | [ "$(cat)" == "200" ] && curl -s $1

