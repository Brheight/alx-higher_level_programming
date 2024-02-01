#!/bin/bash
# This script takes a URL as an argument, sends an OPTIONS request using curl, and displays the allowed HTTP methods.
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d ' ' -f 2-
