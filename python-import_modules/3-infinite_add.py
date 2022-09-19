#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print(sum(map(lambda x: int(x), sys.argv[1:])))
