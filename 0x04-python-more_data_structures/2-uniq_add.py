#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = []
    for i in my_list:
        if i not in res:
            res.append(i)
    res = sum(res)
    return(res)
