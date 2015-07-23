from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('points', '/points.json')
    config.add_route(
        'points_extent', '/points/{xmin},{ymin},{xmax},{ymax}.json')
    config.add_route('point', '/points/{id}.json')
    config.add_route('point_add', '/points')
    config.add_route('imprint', '/imprint')
    config.scan()
    return config.make_wsgi_app()
