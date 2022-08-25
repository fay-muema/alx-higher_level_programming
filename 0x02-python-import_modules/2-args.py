#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = len(sys.argv) - 1
    
    if arg == 0:
        print("{} argument:".format(arg))

    elif arg == 1:
        print("{} argument:".format(arg))
    else:
        print("{} argument:".format(arg))

    if arg >= 1:
        arg = 0

        for i in sys.argv:
            if arg != 0:
                print("{}: {}".format(arg, i))

            arg += 1
