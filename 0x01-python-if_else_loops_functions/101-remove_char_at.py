#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    j = 0
    for i in str:
        if j != n:
            new += str[j]
        j += 1
    return new
