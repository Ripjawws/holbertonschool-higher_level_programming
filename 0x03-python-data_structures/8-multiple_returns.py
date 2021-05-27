#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0] if sentence else None
    new_tuple = (lenght, first)
    return new_tuple
