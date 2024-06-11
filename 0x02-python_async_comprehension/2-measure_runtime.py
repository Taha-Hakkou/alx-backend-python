#!/usr/bin/env python3
""" 2-measure_runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures runtime for multiple
    async_comprehensions running in parallel """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start
    return total_time
