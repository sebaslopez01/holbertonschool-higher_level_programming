#!/usr/bin/python3


def uppercase(str):
    upper_c: str

    for c in str:
        asc_c = ord(c)
        if asc_c >= 97 and asc_c <= 122:
            upper_c = chr(asc_c - 32)
        else:
            upper_c = c
        print(upper_c, end="")

    print()
