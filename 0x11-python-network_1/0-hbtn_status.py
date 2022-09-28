#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    result = response.read()
    print("Body response:")
    print(" - type: {}".format(type(result)))
    print(" - content: {}".format(result))
    print(" - utf-8 content: {}".format(result.decode('utf-8')))
