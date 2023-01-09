#!/usr/bin/env python3
'''
    Module Task to import wait_random from 
    the previous python file and write an async routine 
    called wait_n that takes in 2 int arguments 
    (in this order): n and max_delay.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    To execute wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
