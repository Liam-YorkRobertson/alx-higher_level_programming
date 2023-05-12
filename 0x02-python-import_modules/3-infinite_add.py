#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argu = sys.argv
    argLen = len(argu) - 1
    if argLen == 0:
        print("{:d}".format(argLen))
    elif argLen > 0:
        i = 1
        j = 0
        while (i < argLen + 1):
            j = j + int(argu[i])
            i = i + 1  # same as i++ in C
        print("{:d}".format(j))
