#!/bin/bash
# Script to send a GET request with a specific header and display the response body
curl -sH "X-School-User-Id: 98" "$1"
