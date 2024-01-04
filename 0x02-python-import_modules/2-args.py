#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = (sys.argv)[1:]
    size = len(args)
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print(f"{size} argument:")
    else:
        print(f"{size} arguments:")
    if size > 0:
        for i in range(size):
            print("{}: {}".format((i + 1), args[i]))
