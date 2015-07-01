from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.mako')
def index(request):
    return {}
