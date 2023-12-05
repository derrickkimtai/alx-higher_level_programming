#!/bin/bash

# Sends a JSON POST request to a URL passed as the first argument with the file contents as the request body

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url=$1
filename=$2

curl -s -X POST -H "Content-Type: application/json" -d "@$filename" "$url"
