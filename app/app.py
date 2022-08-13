from aiohttp import web
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import json_response


async def ping(request):

    req = request.headers['User-Agent']
    return {'message': 'pong'}, f'{req}'


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[middleware])
app.router.add_route('GET', "/ping", ping)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")
