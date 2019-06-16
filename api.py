import json

from aiohttp import web_request, web


async def health(request: web_request):
    response = json.dumps({'status': 'ok'})
    return web.Response(body=response)


async def check_password(request: web_request):
    submission = await request.json()
    error_messages = {
        1: "Password is too short",
        2: "Password is barely even a word",
        3: "You can do better",
        4: "Four-lettered words are not allowed, don't be rude",
        5: "Do not use your dog's name"
    }

    password_length = len(submission['password'])

    if password_length == 0:
        error_message = ''
        is_valid = True
    elif password_length < 6:
        error_message = error_messages[password_length]
        is_valid = False
    else:
        error_message = "Password too hard to remember"
        is_valid = False

    response = json.dumps({'isValid': is_valid, 'errorMessage': error_message})
    return web.Response(body=response, content_type='application/json')

