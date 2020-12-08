#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            j = ord(str[i]) - 32
        print("{}".format(chr(j)), end='')
    print("")
