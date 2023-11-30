#!/bin/bash
#check if an argunment is provided
if [$# -ne 1]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
#get the URL from the argunment
url=$1

curl -sI "$url" | awk '/Content-Length/ {print $2}'

