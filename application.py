from aiohttp import web
import settings
from api import health


def set_routes(app):
    add_route = app.router.add_route
    add_route('GET', '/', health)


application = web.Application()
set_routes(application)

if __name__ == "__main__":
    web.run_app(application, port=settings.HTTP_PORT, access_log=None)
else:
    # We're in docker-land. Let gunicorn handle the rest
    pass
