import os
import sys

_DEFAULTS = {
    'HTTP_PORT': 8080,
    'FRONTEND_HOST': 'http://localhost:3000'
}

for k, v in _DEFAULTS.items():
    sys.modules[__name__].__dict__[k] = os.environ.get(k, v)
