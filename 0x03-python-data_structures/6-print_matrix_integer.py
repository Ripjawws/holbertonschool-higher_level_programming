#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print("{}".format(matrix[i][j]), end=' ')
        if matrix[0]:
            print("{}".format(matrix[i][-1]))
        else:
            print()
