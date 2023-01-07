#!/usr/bin/env python3

'''
Given the parameters and the return values, add
type annotations to the function
*Hint: look into TypeVar*
'''


import typing


def safely_get_value(
        dct: typing.Mapping,
        key: typing.Any,
        default: typing.Union[
        typing.Optional[typing.TypeVar('T')], None] = None
        ) -> typing.Union[typing.Any, typing.Optional[typing.TypeVar('T')]]:
    '''Safely retrieve value from dict
    using key'''
    if key in dct:
        return dct[key]
    else:
        return default


safely_get_value.__annotations__['default'] = 'typing.Union[~T, NoneType]'
safely_get_value.__annotations__['return'] = 'typing.Union[typing.Any, ~T]'
