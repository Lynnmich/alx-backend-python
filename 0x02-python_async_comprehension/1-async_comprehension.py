#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using async comprehension,
    and returns the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
