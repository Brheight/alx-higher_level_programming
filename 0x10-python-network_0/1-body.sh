#!/bin/bash
# This script takes a URL as an argument, sends a silent GET request using curl, and displays the body of the response for a 200 status code.
curl -sL -w "%{http_code}" "$1" -o /dev/null | [ "$(tail -c 3)" == "200" ] && curl -sL "$1" || true
