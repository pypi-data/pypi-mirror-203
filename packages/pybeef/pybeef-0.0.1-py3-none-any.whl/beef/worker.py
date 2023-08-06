from beef import beef
import asyncio

@beef(queue_name='worker')
async def worker(a: int, b:int) -> int:
    await asyncio.sleep(1)
    await worker.set_progress(steps=10, progress=1)
    await asyncio.sleep(1)
    await worker.set_progress(steps=10, progress=2)
    await asyncio.sleep(1)
    await worker.set_progress(steps=10, progress=3)
    return a + b