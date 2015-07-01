from pyramid.view import view_config
from reportr.models import DBSession, Point
from geoalchemy2.shape import to_shape


@view_config(route_name='home', renderer='templates/index.mako')
def index(request):
    return {}


@view_config(route_name='imprint', renderer='templates/imprint.mako')
def imprint(request):
    return {}


@view_config(route_name='points', renderer='json')
def points(request):
    points = DBSession.query(Point).all()

    points_geojson = []
    for point in points:
        # convert from WKB to a Shapely geometry
        geom = to_shape(point.geom)

        points_geojson.append({
            'type': 'Feature',
            'properties': {
                'id': point.id,
                'title': point.title,
                'date': str(point.date)
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    geom.x,
                    geom.y
                ]
            }
        })

    return {
        'type': 'FeatureCollection',
        'features': points_geojson
    }
