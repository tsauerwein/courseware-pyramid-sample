from pyramid.view import view_config
from reportr.models import DBSession, Point
from geoalchemy2.shape import to_shape
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from sqlalchemy.orm.exc import NoResultFound


@view_config(route_name='home', renderer='templates/index.mako')
def index(request):
    return {}


@view_config(route_name='imprint', renderer='templates/imprint.mako')
def imprint(request):
    return {}


@view_config(route_name='points', renderer='json')
def points(request):
    points = DBSession.query(Point).all()
    points_geojson = [to_geojson(point) for point in points]

    return {
        'type': 'FeatureCollection',
        'features': points_geojson
    }


@view_config(route_name='point', renderer='json')
def point(request):
    try:
        # try to cast the given id to an integer
        id = int(request.matchdict['id'])
    except ValueError:
        raise HTTPBadRequest()

    try:
        # load the point with the given id
        point = DBSession.query(Point).filter(Point.id == id).one()
    except NoResultFound:
        raise HTTPNotFound()

    return to_geojson(point)


def to_geojson(point):
    # convert from WKB to a Shapely geometry
    geom = to_shape(point.geom)

    return {
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
    }
