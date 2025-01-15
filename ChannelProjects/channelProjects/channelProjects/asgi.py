"""
ASGI config for channelProjects project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chats.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelProjects.settings")

django_asgi_app  = get_asgi_application()
print(django_asgi_app , websocket_urlpatterns)
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    ),
    # Just HTTP for now. (We can add other protocols later.)
})