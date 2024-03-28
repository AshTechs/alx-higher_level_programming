#!/bin/bash
# Takes a URL, sends a GET request, and displays the response.
curl -s -o response.txt -w "%{http_code}" $1 | awk 'NR==1{if($1 == 200) {getline; print}}'
