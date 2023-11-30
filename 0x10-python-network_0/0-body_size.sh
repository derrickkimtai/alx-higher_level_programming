#!/bin/bash
#get the URL from the argunment
curl -s "$1" | wc -c
