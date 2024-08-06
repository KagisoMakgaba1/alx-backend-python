#!/usr/bin/env python3

"""
Project details:

Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension over
async_generator, then return the 10 random numbers.
"""

from typing import Callable, List

async_generator: Callable = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Uses Async comprehension to iterate over a generator and returns a list
    of float values.
    """

    return [_ async for _ in async_generator()]
