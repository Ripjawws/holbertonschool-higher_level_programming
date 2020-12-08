#!/usr/bin/python3
for counter in range(0, 100):
    if counter < 99:
        print("{:02d}, ".format(counter), end='')
    else:
        print("{:02d}".format(counter))
