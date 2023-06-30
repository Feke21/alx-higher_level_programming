#!/bin/bash
#Makes request to 0.0.0.0:5000/catch_me that causes server to respond with message You got me! in body of the response
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:HolbertonSchool"
