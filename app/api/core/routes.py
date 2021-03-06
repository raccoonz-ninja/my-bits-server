import app.api.address as address
import app.api.bitcoin as bitcoin
import app.api.device as device
import app.api.user as user


def handle_404(request):
    return dict(error='Unknown route')

def handle_ping(request):
    return dict(status='ok')

def wire_route(config, path=None, handler=None, renderer='json', request_method='POST'):
    route_name = path
    config.add_route(route_name, path, request_method=request_method)
    config.add_view(handler, route_name=route_name, renderer=renderer)


def wire_routes(config):
    wire_route(config, path='/api/{api_version}/user/register', handler=user.register)
    wire_route(config, path='/api/{api_version}/user/{user_id}/device/register', handler=device.register)
    wire_route(config, path='/api/{api_version}/user/{user_id}/address/add', handler=address.add)
    wire_route(config, path='/api/{api_version}/bitcoin/xpub', handler=bitcoin.generate, request_method='GET')
    wire_route(config, path='/ping', handler=handle_ping, request_method='GET')

    config.add_view(handle_404, renderer='json', context='pyramid.httpexceptions.HTTPNotFound')
