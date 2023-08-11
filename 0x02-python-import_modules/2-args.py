#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("{:d} arguments.".format(0))
    else:
        print("{:d} arguments:".format(num_args))
        for i, args in enumerate(args, start=1):
            print("{:d}: {}".format(i, args))
