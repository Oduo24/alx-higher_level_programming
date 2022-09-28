#!/usr/bin/python3
"""1-hbtn_header module"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    with urlopen(argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
