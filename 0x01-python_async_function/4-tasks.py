#!/usr/bin/env python3
""" 4-tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ identical to wait_n except task_wait_random is being called """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    return await asyncio.gather(*tasks)
