#!/usr/bin/bash
#Takes in a URL, sends a request and displays the size of the response
curl -sI $1 | grep "Content-Length:" | cut -c 17-
