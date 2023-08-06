from __future__ import annotations

__all__ = ["run_in_thread_pool"]

import asyncio
import functools
import threading
import logging
from typing import Callable, Coroutine
from concurrent.futures import ThreadPoolExecutor


from .worker import Context

logger: logging.Logger = logging.getLogger(name="pool_cue")

THREAD_POOL_EVENT_LOOPS: dict[int, asyncio.AbstractEventLoop] = {}


def _run_coro_in_thread_pool(coro: Callable, *args, **kwargs) -> None:
    """
    Function used by 'run_in_thread_pool' to support running asynchronous functions in sub threads:
    Creates a new event loop in the current (sub) thread (if one doesn't already exist)
    to make it possible to call async functions.

    Based on:
    https://stackoverflow.com/questions/46074841/why-coroutines-cannot-be-used-with-run-in-executor/63106889#63106889
    """
    current_thread_id: int = threading.current_thread().ident
    loop: asyncio.AbstractEventLoop
    if current_thread_id in THREAD_POOL_EVENT_LOOPS:
        loop = THREAD_POOL_EVENT_LOOPS[current_thread_id]
    else:
        logger.debug("Creating new event loop in sub thread %s...", current_thread_id)
        loop = asyncio.new_event_loop()
        THREAD_POOL_EVENT_LOOPS[current_thread_id] = loop
    future: Coroutine = coro(*args, **kwargs)
    return loop.run_until_complete(future=future)


async def run_in_thread_pool(ctx: Context, func: Callable, *args, **kwargs) -> None:
    """
    Run the given function in the queue worker's dedicated thread pool.
    Use this to run I/O bound tasks without blocking the worker's main thread.

    Supports both synchronous and asynchronous functions.

    :param ctx: The worker context.
    :param func: The function you want to run in a sub thread.
    :param args: Extra positional arguments that will be passed to the task function.
    :param kwargs: Extra keyword arguments that will be passed to the task function.
    """
    loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
    thread_pool: ThreadPoolExecutor = ctx["pool"]
    if asyncio.iscoroutinefunction(func=func):
        await loop.run_in_executor(
            executor=thread_pool, func=functools.partial(_run_coro_in_thread_pool, coro=func, *args, **kwargs)
        )
    else:
        await loop.run_in_executor(executor=thread_pool, func=functools.partial(func, *args, **kwargs))
