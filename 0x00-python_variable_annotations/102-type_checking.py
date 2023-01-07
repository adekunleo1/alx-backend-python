#!/usr/bin/env python3

'''
Use `mypy` to validate the following
piece of code and apply any necessary changes.
'''


import typing
from typing import Tuple, List


def zoom_array(lst: List, factor: typing.Union[int, float] = 2) -> List:
    '''Zoom Array Docstrings'''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


zoom_array.__annotations__ = {
    'lst': 'typing.Tuple',
    'factor': "<class 'int'>",
    'return': "typing.List"
}

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
