#!/usr/bin/env python3
"""Function that takes wait_n and alters it into a new function"""
import asyncio
from asyncio.tasks import Task
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delays"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
