#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response with a second argument containing a file to post
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
