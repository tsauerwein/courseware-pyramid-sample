import os
import sys
import transaction
from datetime import datetime

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Point,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        DBSession.add(
            Point(title='Broken street-light', date=datetime.now(), geom='SRID=4326;Point(8.538265 47.394572)'))
        DBSession.add(
            Point(title='Potholes', date=datetime.now(), geom='SRID=4326;Point(8.516206 47.390098)'))
        DBSession.add(
            Point(title='Graffiti', date=datetime.now(), geom='SRID=4326;Point(8.538866 47.375802)'))
        DBSession.add(
            Point(title='Broken street-light', date=datetime.now(), geom='SRID=4326;Point(8.529853 47.383357)'))
