#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.get(key) is not None and a_dictionary.pop(key)
    return a_dictionary
