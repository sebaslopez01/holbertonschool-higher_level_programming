#!/usr/bin/python3

for i in reversed(range(97, 123)):
    char = chr(i)
    if i % 2 != 0:
        char = chr(i - 32)
    print("{}".format(char), end="")
