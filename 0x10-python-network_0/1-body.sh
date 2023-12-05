#!/bin/bash
url=$1

response=$(curl -s -o /dev/null -w "%{http_code}" "url")

if [ $response -eq 200 ]; then
	body=$(curl -s $url)
	echo "$body"
else
	echo "Error"
fi
