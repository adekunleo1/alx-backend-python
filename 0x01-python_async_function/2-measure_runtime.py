#!/usr/bin/env python3
'''
    Module that import wait_n into 2-measure_runtime.py
    from the previous file.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    To create an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
