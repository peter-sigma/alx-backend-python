#!/usr/bin/env python3
"""
    Asynchronous coroutine that takes an integer,
    waits for a random no of seconds and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ 
        Waits for a random number of seconds 
    """
    wait_seconds = random.uniform(0, max_delay)
    await asyncio.sleep(wait_seconds)
    return wait_seconds
