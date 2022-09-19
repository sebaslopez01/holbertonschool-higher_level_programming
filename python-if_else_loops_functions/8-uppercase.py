#!/usr/bin/python3


def uppercase(str):
    for c in str:
        asc_c = ord(c)
        if asc_c >= 97 and asc_c <= 122:
            c = chr(asc_c - 32)

        print("{}".format(c), end="")

    print()
