#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    a = 0
    b = 0
    ret = []
    for i in range(2):
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        ret.append(a + b)
    new_tuple = ret[0], ret[1]
    return new_tuple
