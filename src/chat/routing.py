from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatapp.routing

application = ProtocolTypeRouter({
	# (https->django views is added by default)
	'websocket': AuthMiddlewareStack(
		URLRouter(
			chatapp.routing.websocket_urlpatterns
		)
	),
})
