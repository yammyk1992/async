from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.post('/')
@route.get('/')
async def index(request: Request):
    return 'Hello World!'
