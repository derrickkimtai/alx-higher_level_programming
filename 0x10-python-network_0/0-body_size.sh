#!/bin/bash
#get the URL from the argunment
curl -sI "$1" | awk '/Content-Length/ {print $2}'
