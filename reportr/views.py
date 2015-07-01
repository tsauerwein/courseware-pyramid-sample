from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.mako')
def index(request):
    points = [
        {'title': 'Broken street-light', 'lon': 8.538265, 'lat': 47.394572},
        {'title': 'Potholes', 'lon': 8.516206, 'lat': 47.390098},
        {'title': 'Graffiti', 'lon': 8.538866, 'lat': 47.375802},
        {'title': 'Broken street-light', 'lon': 8.529853, 'lat': 47.383357}
    ]

    return {
        'points': points
    }
