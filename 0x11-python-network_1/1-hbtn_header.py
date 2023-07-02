#!/usr/bin/python3
"""
display value of the X-Request-Id var in header of the response.
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
