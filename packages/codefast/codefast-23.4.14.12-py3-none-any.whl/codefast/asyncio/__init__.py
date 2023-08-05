#!/usr/bin/env python
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Callable
from codefast.utils import shell
import warnings


async def async_render(sync_func: Callable, *args, **kwargs):
    warnings.warn("This function is deprecated. Use asyncformer() instead.", DeprecationWarning)
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, sync_func, *args, **kwargs)


async def asyncformer(sync_func: Callable, *args, **kwargs):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, sync_func, *args, **kwargs)


def run_async_script(python_file: str):
    which_python = sys.executable
    return shell(f"{which_python} {python_file}")
