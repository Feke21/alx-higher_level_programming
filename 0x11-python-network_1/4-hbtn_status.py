#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status with package Requests
"""


if __name__ == '__main__':
    from requests import get

    html = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
