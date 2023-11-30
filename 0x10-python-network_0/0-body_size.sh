#!/bin/bash
#get the URL from the argunment
url=$1

curl -sI "$url" | awk '/Content-Length/ {print $2}'

