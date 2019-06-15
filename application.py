import argparse
from aiohttp import web
import aiohttp_jinja2
import jinja2
import api
import settings
import logger


def setroutes(app):
    add_route = app.router.add_route
    add_route('GET', '/', api.health)

    app.add_routes([web.static('/css', "static/css")])
    app.add_routes([web.static('/img', "static/img")])
    app.add_routes([web.static('/js', "static/js")])


def process_args():
    parser = argparse.ArgumentParser(description='Run an HTTP server for the MSTeams Integration Service.')
    parser.add_argument('--path', help="Path to unix socket. If left out, will bind to 0.0.0.0"
                                       " (all interfaces).")
    parser.add_argument('--port', help="TCP port to run on", type=int)

    args = parser.parse_args()
    if args.path is not None:
        settings.SOCKET_PATH = args.path
    if args.port is not None:
        settings.HTTP_PORT = args.port
    return args


if __name__ == "__main__":
    processed_args = process_args()

    # Start app
    application = web.Application()
    aiohttp_jinja2.setup(application,
                         loader=jinja2.FileSystemLoader('templates/'))

    setroutes(application)
    if settings.SOCKET_PATH:
        web.run_app(application, path=settings.SOCKET_PATH, access_log=None)
    else:
        web.run_app(application, port=settings.HTTP_PORT, access_log=None)
