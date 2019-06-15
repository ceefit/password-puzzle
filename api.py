import json

from aiohttp import web_request, web


async def health(request: web_request):
    response = json.dumps({'status': 'ok'})
    return web.Response(body=response)

