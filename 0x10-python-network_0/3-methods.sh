#!/bin/bash
#Takes in a url and displays the http methods allowed by the server
curl -sIL -X OPTIONS $1 | grep "Allow:" | cut -c 8-
