#!/usr/bin/env python3

"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""

import asyncio
from typing import Callable

wait_random: Callable = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function returns an asyncio.Task object that will wait for a random
    delay between 0 and max_delay seconds and then return the delay time.
    """

    return asyncio.create_task(wait_random(max_delay))
