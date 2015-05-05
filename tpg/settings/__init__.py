import socket

PRODUCTION_HOST = [
    'p1',
    'p2',
]

if socket.gethostname() in PRODUCTION_HOST:
    from tpg.settings.production import *
else:
    from tpg.settings.local import *
