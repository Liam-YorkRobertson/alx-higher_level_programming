#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argu = sys.argv
    argLen = len(argu) - 1
    if (argLen == 0):
        print("{:d} arguments.".format(argLen))
    elif (argLen == 1):
        print("{:d} argument:".format(argLen))
        print("{:d}: {}".format(argLen, argu[1]))
    elif (argLen > 1):
        print("{:d} arguments:".format(argLen))
        for i in range(1, argLen + 1):
            print("{:d}: {}".format(i, argu[i]))
