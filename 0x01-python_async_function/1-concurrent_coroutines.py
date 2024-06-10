#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ pawn wait_random n times with the specified max_delay """
    aws = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*asyncio.as_completed(aws))
