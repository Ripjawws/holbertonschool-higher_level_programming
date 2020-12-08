#!/usr/bin/python3
for first in range(0, 10):
    second = first + 1
    for second in range(second, 10):
        print("{:d}".format(first), end='')
        if first == 8 and second == 9:
            print("{:d}".format(second))
        else:
            print("{:d}, ".format(second), end='')
