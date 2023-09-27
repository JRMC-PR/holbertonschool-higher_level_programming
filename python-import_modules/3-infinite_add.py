#!/usr/bin/python3
if __name__ == "__main__":
    import sys
# initialize sum
sum = 0
argc = len(sys.argv)  # ? retrive the number of elements in argv
if argc == 1:
    print("0")
else:
    # ? sum all argumentds and print
    for i in range(1, argc):
        sum += int(sys.argv[i])
    print(sum)
