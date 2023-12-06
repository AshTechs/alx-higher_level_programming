#!/usr/bin/python3
def print_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item < len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print(f"{matrix[row][item]:d}", end=endspace)
            print()
