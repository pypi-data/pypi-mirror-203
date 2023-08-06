import asyncio
from typing import Optional

class Latch:
    def __init__(self, concurrency: int = 1):
        self.concurrency = concurrency
        self.qsize = 0
        self.latch = asyncio.Queue(maxsize=concurrency)

    async def __aenter__(self):
        await self.latch.put(1)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.latch.get_nowait()


class Progress:
    def __init__(self, beef, loop):
        self._beef = beef
        self._loop = loop

    def __call__(self, *, steps=0, progress=-1, message: Optional[str] = None):
        coro = self._beef.set_progress(steps=steps, progress=progress, message=message)
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return future.result()