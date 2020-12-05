#!/usr/bin/env python3
import sys

def add(i=3, j=4):
    """
    add two numbers
    """
    return i + j

if __name__ == "__main__":
    if len(sys.argv)!=3:
        raise Exception("need to pass 2 args, both int")
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        arg1_int = int(arg1)
    except ValueError:
        print("arg1 is not an int")
    try:
        arg2_int = int(arg2)
    except ValueError:
        print("arg2 is not an int")

    result = add(arg1_int, arg2_int)
    #print(result)
    sys.exit(result)
