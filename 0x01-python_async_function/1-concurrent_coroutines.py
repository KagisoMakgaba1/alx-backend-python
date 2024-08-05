#!/usr/bin/env python3

"""
Task details:

Import `wait_random` from the previous python file that you've written and
write an async routine called `wait_n` that takes in 2 int arguments (in this
order): `n` and `max_delay`. You will spawn `wait_random` n times with the
specified `max_delay`.

`wait_n` should return the list of all the delays (float values). The list of
the delays should be in ascending order without using `sort()` because of
concurrency.
"""

import asyncio
from typing import List, Callable


wait_random: Callable = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns a list of n random float numbers between 0 and
    max_delay.
    """

    delays: List[float] = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]
    return [await delay for delay in asyncio.as_completed(delays)]
