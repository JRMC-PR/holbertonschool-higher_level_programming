#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):  # len(row) is the number of columns
            if i == 0:
                print("{:d}".format(row[i]), end="")
            else:
                print(" {:d}".format(row[i]), end="")
        print()
