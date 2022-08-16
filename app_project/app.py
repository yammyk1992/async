from aiohttp import web
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import json_response

from app_project.api.v1 import app as v1_app
from app_project.api.v2 import app as v2_app
from app_project.api.healthcheck import route as healthcheck_route
from app_project.api.index import route as index_route


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])

app.router.add_routes(index_route)
app.router.add_routes(healthcheck_route)

app.add_subapp('/v1', v1_app)
app.add_subapp('/v2', v2_app)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")
