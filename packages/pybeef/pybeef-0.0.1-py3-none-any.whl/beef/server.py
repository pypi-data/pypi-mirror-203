from .worker import worker

async def server():
    async with worker.connect('amqp://localhost/'):
        await worker.serve()

if __name__ == '__main__':
    import asyncio

    asyncio.run(server())
