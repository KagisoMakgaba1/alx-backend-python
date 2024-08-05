#!/usr/bin/env python3

"""
Task details:

Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""

from typing import List, Callable
import asyncio


task_wait_random: Callable = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns a list of n random float numbers between 0 and
    max_delay.
    """

    delays: List[float] = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
