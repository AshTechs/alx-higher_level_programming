#!/usr/bin/python3
def remove_char_at(str, i):
    if i < 0:
        return str
    else:
        str = str[0:i] + str[i+1:]
    return str
