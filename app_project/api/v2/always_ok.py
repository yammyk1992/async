from aiohttp import web
from aiohttp.web_request import Request

route = web.RouteTableDef()


@route.get('/always_ok')
async def health(request: Request):
    return {'message': "I'm always not ok"}
