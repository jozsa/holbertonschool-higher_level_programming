#!/bin/bash
# Curl a URL passed in and display size of body of response
curl -s "$1" | wc -c
