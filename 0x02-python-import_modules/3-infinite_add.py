#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = (sys.argv)[1:]
    size = len(args)
    sum = 0
    if size > 0:
        for i in range(size):
            sum += int(args[i])
    print(sum)
