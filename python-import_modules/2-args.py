#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    count = len(argv)

    if count == 0:
        print("{} arguments.".format(count))
    else:
        word = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, word))

        for index, arg in enumerate(argv, start=1):
            print("{}: {}".format(index, arg))


if __name__ == "__main__":
    main()
