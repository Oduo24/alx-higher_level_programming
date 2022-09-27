#!/bin/bash
#Takes in a url and displays the http methods allowed by the server
curl -sIL -X OPTIONS google.com | grep "Allow:" | cut -d':' -f2 | sed "s/ //"
