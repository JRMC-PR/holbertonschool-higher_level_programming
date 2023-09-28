#!/usr/bin/python3
if __name__ == "__main__":
    import sys
# * asigne values to argv and argc
argc = len(sys.argv)  # ? retrive the number of elements in argv
if argc == 1:
    print("0 arguments.")
else:
    # ? check argc and print print the number of arguments
    print(f"{argc - 1} argument{'s' if argc > 2 else ''}:")
# * print the arguments
for i in range(1, argc):
    print(f"{i}: {sys.argv[i]}")
