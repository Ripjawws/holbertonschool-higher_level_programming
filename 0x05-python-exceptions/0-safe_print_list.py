#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    new_str = ""
    for i in my_list[:x]:
        new_str += str(i)
        j += 1
    try:
        print(new_str)
        return j
    except:
        print(Error)
        