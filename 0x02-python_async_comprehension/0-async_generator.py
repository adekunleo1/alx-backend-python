#!/usr/bin/env python3
""" a python module to loop 10 times """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator - function to loop 10x
    wait 1 seconds, then yield a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
