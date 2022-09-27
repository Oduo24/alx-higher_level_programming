#!/bin/bash
#Displays only the body of a URL passed as argument
if [ $(curl -s -L -w "%{http_code}" $1 -o ~/devfile) -eq 200 ]; then curl -sL $1; fi
