from aiohttp import web
from api import health, check_password
import aiohttp_cors
import settings


def set_routes(app):
    application_cors = aiohttp_cors.setup(app)
    check_password_resource = application_cors .add(app.router.add_resource("/check-password"))
    check_password_route = application_cors.add(
        check_password_resource.add_route("POST", check_password), {
            "http://localhost:3000": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers=("X-Custom-Server-Header",),
                allow_headers=("X-Requested-With", "Content-Type"),
                max_age=3600,
            )
        })

    add_route = app.router.add_route
    add_route('GET', '/', health)


application = web.Application()
cors = aiohttp_cors.setup(application)
set_routes(application)

if __name__ == "__main__":
    web.run_app(application, port=settings.HTTP_PORT, access_log=None)
else:
    # We're in docker-land. Let gunicorn handle the rest
    pass
