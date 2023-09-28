#!/bin/bash
# a Bash script that takes and  sends a request to URL, and displays the body size of the response
curl -sI "$1" | grep -i "Content-length" | cut -d " " -f2
