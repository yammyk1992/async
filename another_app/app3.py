import asyncio
from datetime import time

from aiohttp import web, request
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from part1.sites import sites

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0)" \
             "Gecko/20100101 Firefox/103.0"

check_background_task = {}


async def say_hello(request: Request):
    return {'massage': 'HeLLo My Friend!!!'}


async def background_task():
    while True:
        pending = [asyncio.create_task(send_request(site)) for site in sites]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            task_result = done.pop().result()
            url, status = task_result

            check_background_task[url] = {
                'status': status,
                'time': time(),
            }

        print(time(), 'Background task iteration done')
        await asyncio.sleep(10)


async def start_background_tasks(app):
    app['background_tasks'] = asyncio.create_task(background_task())


async def send_request(url):
    async with request('GET', url, headers={'User-Agent': user_agent}) as response:
        return url, response.status


async def ping(request: Request):
    return check_background_task


async def health(request: Request):
    print(asyncio.all_tasks())
    return {'message': 'ok'}


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])
app.router.add_route('GET', "/", say_hello)
app.router.add_route('GET', "/ping", ping)
app.router.add_route('GET', "/health", health)
app.on_startup.append(start_background_tasks)

if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0")
