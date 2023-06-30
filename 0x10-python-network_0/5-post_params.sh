#!/bin/bash
#Takes URL, send POST request to it & display body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
