from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.get('/health')
@route.post('/new_health')
async def health(request: Request):
    return {'message': 'ok'}