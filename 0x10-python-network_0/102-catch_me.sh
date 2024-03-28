#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond.
curl -s -X PUT -d "user_id=98" "http://0.0.0.0:5000/catch_me" -D - -o /dev/null
