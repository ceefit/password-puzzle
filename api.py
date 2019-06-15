from aiohttp import web_request, web


async def health(request: web_request):
    return web.Response(text="OK")

