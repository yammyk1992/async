import asyncio
from aiohttp import web, request
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from part1.sites import sites

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0)" \
             "Gecko/20100101 Firefox/103.0"


async def say_hello(request: Request):
    return {'massage': 'HeLLo My Friend!!!'}


async def send_request(url):
    async with request('GET', url, headers={'User-Agent': user_agent}) as response:
        return url, response.status


async def ping(request: Request):
    result = {}

    tasks = [send_request(site) for site in sites]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    for task in done:
        url, status = task.result()
        result[url] = status

    return result


async def health(request: Request):
    return {'message': 'ok'}


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])
app.router.add_route('GET', "/", say_hello)
app.router.add_route('GET', "/ping", ping)
app.router.add_route('GET', "/health", health)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")
