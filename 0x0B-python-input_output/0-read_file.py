#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """read_file function
    this function reads file with 'filename' arg
    """

    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end='')
