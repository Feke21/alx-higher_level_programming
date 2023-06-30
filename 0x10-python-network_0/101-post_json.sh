#!/bin/bash
#Sends a JSON POST request to a URL passed as first argument, displays body of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
