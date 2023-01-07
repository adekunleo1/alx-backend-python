#!/usr/bin/env python3

'''
**Task Instructions**: Annotate the below
function’s parameters and return values
with the appropriate types
'''


import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    '''Return a list of tuple containing the element
    and the its length'''
    return [(i, len(i)) for i in lst]
