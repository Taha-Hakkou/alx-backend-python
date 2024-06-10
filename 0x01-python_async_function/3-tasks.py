#!/usr/bin/env python3
""" 3-tasks """
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ return an asyncio.Task """
    return asyncio.create_task(wait_random(max_delay))
