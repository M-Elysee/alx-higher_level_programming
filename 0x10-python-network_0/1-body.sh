#!/bin/bash
# a Bash script that takes and sends a GET request to the URL, and displays the body of the response
curl -sX GET "$1" -L 200
