import contextlib
import aio_pika
from aio_pika.abc import AbstractRobustConnection
from aio_pika.pool import Pool
import random


async def consume(channel_pool: Pool, queue_name: str) -> None:
    async with channel_pool.acquire() as channel:  # type: aio_pika.Channel
        await channel.set_qos(10)

        queue = await channel.declare_queue(
            queue_name, durable=False, auto_delete=False,
        )

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                print(message.body.decode())
                await message.ack()

async def publish(channel_pool: Pool, queue_name: str, i) -> None:
    async with channel_pool.acquire() as channel:  # type: aio_pika.Channel
        await asyncio.sleep(random.random())
        await channel.default_exchange.publish(
            aio_pika.Message(f'{i}: channel {id(channel)}'.encode()),
            queue_name,
        )

async def main() -> None:
    queue_name = 'testing_pool'
    connection: AbstractRobustConnection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel_pool = Pool(connection.channel, max_size=10)

    async with connection, channel_pool:
        task = asyncio.create_task(consume(channel_pool, queue_name))  # start consumer server
        await asyncio.gather(*[publish(channel_pool, queue_name, i) for i in range(100)])  # run produces in parallel
        await asyncio.sleep(2)  # wait for messages to be consumed
        task.cancel()  # tell consumer server to cancel
        with contextlib.suppress(asyncio.CancelledError):
            await task  # wait for consumer server to return its channel(s) to the pool
        # now, close channel_pool and then connection


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())