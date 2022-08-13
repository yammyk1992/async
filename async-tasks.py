import asyncio
from time import time
import aiohttp


async def task(link):
    print(f"start task for {link}, {time()}")

    async with aiohttp.ClientSession().get(link) as response:
        print(response.status)
        print(await response.text())

    print(f"Task {link} done, {time()}")


if __name__ == '__main__':
    tasks = [task(link) for link in ('https://petstore.swagger.io/#/', 'https://google.com', 'https://habr.com')]
    asyncio.run(asyncio.wait(tasks))
