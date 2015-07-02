from pyramid.view import view_config
from reportr.models import DBSession, Point
from geoalchemy2.shape import to_shape, from_shape
from shapely.geometry import Point as PointShape
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime


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


@view_config(route_name='point_add', request_method='POST', renderer='json')
def point_add(request):
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    try:
        # try to get the input parameters
        lon = float(request.POST.get('lon'))
        lat = float(request.POST.get('lat'))
    except ValueError:
        raise HTTPBadRequest()

    point = Point(
        title=title,
        description=description,
        date=datetime.now(),
        geom=from_shape(PointShape(lon, lat), srid=4326))

    DBSession.add(point)

    # flush the session so that the point gets its id
    DBSession.flush()

    return to_geojson(point)


def to_geojson(point):
    # convert from WKB to a Shapely geometry
    geom = to_shape(point.geom)

    return {
        'type': 'Feature',
        'properties': {
            'id': point.id,
            'title': point.title,
            'description': point.description,
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
