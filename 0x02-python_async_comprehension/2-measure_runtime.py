#!/usr/bin/env python3

"""
Project details:

Import `async_comprehension` from the previous file and write a measure_runtime
coroutine that will execute `async_comprehension` four times in parallel using
`asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

My answer:

It is roughly 10 seconds because all of the tasks are being ran at almost
about the same time. The `async_comprehension` function calls the
`async_generator` function which waits 1 second, then yields a random number.
It does this 10 times.

Since the tasks are all being ran in 'parallel', they are all spawned at the
same time, so they all take about the same time to complete.
"""

import asyncio
from time import time
from typing import Callable

async_comprehension: Callable = __import__(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronously measures the runtime of executing four `async_comprehension`
    tasks concurrently.

    This function starts a timer, then concurrently executes four instances of
    the `async_comprehension` function using asyncio.gather. It calculates the
    total runtime by subtracting the start time from the current time after
    all async_comprehension tasks have completed.

    Returns:
        float: The total runtime in seconds of executing the
        `async_comprehension` tasks.
    """

    start_time: float = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time() - start_time
