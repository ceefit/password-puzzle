from aiohttp import web
from api import health, check_password, generate_user_id
import aiohttp_cors
import settings


def set_routes(app):
    """
    Set up routes and CORS configuration (for development mode)
    :param app:
    :return:
    """
    application_cors = aiohttp_cors.setup(app)
    cors_config = {
        settings.FRONTEND_HOST: aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("X-Custom-Server-Header",),
            allow_headers=("X-Requested-With", "Content-Type"),
            max_age=3600,
        )
    }

    health_check_resource = application_cors.add(app.router.add_resource("/"))
    check_password_resource = application_cors.add(app.router.add_resource("/check-password"))
    get_user_id_resource = application_cors.add(app.router.add_resource("/user-id"))

    application_cors.add(health_check_resource.add_route("GET", health), cors_config)
    application_cors.add(check_password_resource.add_route("POST", check_password), cors_config)
    application_cors.add(get_user_id_resource.add_route("GET", generate_user_id), cors_config)


application = web.Application()
cors = aiohttp_cors.setup(application)
set_routes(application)

if __name__ == "__main__":
    web.run_app(application, port=settings.HTTP_PORT, access_log=None)
else:
    # We're in docker-land. Let gunicorn handle the rest
    pass
