#!/usr/bin/env python3

'''
Write a type-annotated function `sum_list` which
takes a list `input_list` of floats as argument
and returns their sum as a float.
'''


import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''Sum of list of floats'''
    return sum(input_list)
