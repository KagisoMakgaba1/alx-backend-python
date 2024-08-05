#!/usr/bin/env python3

"""
This module contains a single function that creates an async function that
will wait for a random delay between 0 and 10 seconds and then return the
delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function returns a random float number between 0 and max_delay.
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
