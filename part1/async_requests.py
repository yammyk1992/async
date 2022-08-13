import asyncio
from time import time

import aiohttp

from part1.sites import sites

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0)" \
             "Gecko/20100101 Firefox/103.0"


async def send_request(url):
    start_time = time()

    async with aiohttp.request('GET', url, headers={'User-Agent': user_agent}) as response:
        await response.text()
        print(f'[{url}] Time elapsed: {time() - start_time:.2f}s ({response.status})')


async def main():
    start_time = time()

    tasks = [send_request(site) for site in sites]
    # print(tasks)
    await asyncio.gather(*tasks)

    # for site in sites:
    #     await send_request(site)

    print(f' Total time elapsed: {time() - start_time:.2f}s')


if __name__ == '__main__':
    asyncio.run(main())
