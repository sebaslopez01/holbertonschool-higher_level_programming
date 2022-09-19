#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 0:
        print("{} arguments:".format(len(sys.argv)))
        for i, arg in enumerate(sys.argv, 1):
            print("{}: {}".format(i, arg))
    else:
        print("0 arguments.")
