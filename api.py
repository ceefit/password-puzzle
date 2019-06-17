import json
import pymongo
import random
import uuid

from aiohttp import web_request, web


async def health(request: web_request):
    response = json.dumps({'status': 'ok'})
    return web.Response(body=response)


def validate_length(password):
    error_messages = {
        1: "Password is too short",
        2: "Password is barely even a word",
        3: "You can do better",
        4: "Four-lettered words are not allowed, don't be rude",
        5: "Do not use your dog's name"
    }

    password_length = len(password)

    if password_length == 0 or password_length > 5:
        error_message = ''
        is_valid = True
    else:
        error_message = error_messages[password_length]
        is_valid = False

    return is_valid, error_message


def validate_vowels(password):
    error_message = ''

    if any(vowel in password.lower() for vowel in ['a', 'e', 'i', 'o', 'u']):
        error_message = 'Password can not contain vowels'
        is_valid = False
    elif 'y' in password.lower() and random.randint(0, 5) == 0:  # and sometimes y
        error_message = 'Password can not contain vowels'
        is_valid = False
    else:
        is_valid = True

    return is_valid, error_message


def copy_pasta_detector(user_id, password):
    """
    Checks the password against what the user last submitted to see if they have been copy-pasting passwords.
    We should ever see a difference of one letter added, or one or many characters removed unless they're
    pulling some bullshit.
    :param user_id:
    :param password:
    :return:
    """
    pass


def generate_user_id(request: web_request):
    user_id = str(uuid.uuid4())

    mongo_client = pymongo.MongoClient("mongodb://localhost:27020/", serverSelectionTimeoutMS=1000)
    mongodb = mongo_client["password-puzzle"]
    puzzle_table = mongodb["password-puzzle"]
    puzzle_table.insert_one({'user-id': user_id})

    return web.Response(body=json.dumps({'user-id': user_id}))


async def check_password(request: web_request):
    response = await request.json()
    password = response['password']
    user_id = response['user_id']

    # The pass case, this is the format the frontend needs to see in order to show a successful password entry
    is_valid = True
    error_message = ''

    # Iterate over the validators in this order
    validators = [
        validate_vowels,
        validate_length,
    ]

    # As soon as one validator throws an is_valid is False, return that error message and stop processing further rules
    for validator in validators:
        (is_valid, error_message) = validator(password)
        if is_valid is False:
            break

    response = json.dumps({'isValid': is_valid, 'errorMessage': error_message})
    return web.Response(body=response, content_type='application/json')

