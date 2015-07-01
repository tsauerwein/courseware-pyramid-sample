from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.mako')
def index(request):
    return {}


@view_config(route_name='imprint', renderer='templates/imprint.mako')
def imprint(request):
    return {}


@view_config(route_name='points', renderer='json')
def points(request):
    points = [
        {'title': 'Broken street-light', 'lon': 8.538265, 'lat': 47.394572},
        {'title': 'Potholes', 'lon': 8.516206, 'lat': 47.390098},
        {'title': 'Graffiti', 'lon': 8.538866, 'lat': 47.375802},
        {'title': 'Broken street-light', 'lon': 8.529853, 'lat': 47.383357}
    ]

    points_geojson = [{
        'type': 'Feature',
        'properties': {
            'title': point.get('title')
        },
        'geometry': {
            'type': 'Point',
            'coordinates': [
                point.get('lon'),
                point.get('lat')
            ]
        }
    } for point in points]

    return {
        'type': 'FeatureCollection',
        'features': points_geojson
    }
