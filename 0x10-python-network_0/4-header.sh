#!/bin/bash
# Send custom header with value and display body of response
curl -H "X-HolbertonSchool-User-Id: 98" "$1"
