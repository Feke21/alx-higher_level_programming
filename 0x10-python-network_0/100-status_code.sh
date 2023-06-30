#!/bin/bash
#Sends a request URL passed as an argument, displays the status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
