#!/bin/bash
# send POST request with email and subject, display body of response
curl -s -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
