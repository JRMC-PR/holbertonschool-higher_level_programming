#!/usr/bin/python3
if __name__ == "__main__":
    import sys
# * asigne values to argv and argc
# argv = sys.argv
argc = len(sys.argv)
# * print the number of arguments
print("{} arguments.".format(argc - 1) if argc <=
      1 else "{} argumentss:".format(argc - 1))
# * print the arguments
for i in range(1, argc):
    print("{}: {}".format(i, sys.argv[i]))
