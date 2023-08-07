#!/usr/bin/env python3
"""An asynchronous coroutine that takes 2 arguments"""
import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all the delays(floats) in Ascending order"""
    todos = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await routine for routine in asyncio.as_completed(routines)]
