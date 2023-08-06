from .worker import worker

async def client(*av, **kaw):
    async with worker.connect('amqp://localhost/'):
        task_id = await worker.submit(*av, **kaw)
        print(f'Started task {task_id}')
        while True:
            status = await worker.get_status(task_id=task_id)
            print(status)
            if status.is_final:
                return status
            await asyncio.sleep(1)
            # await worker.cancel(task_id=task_id)

if __name__ == '__main__':
    import asyncio

    result = asyncio.run(client(1, 2))
    print(result)