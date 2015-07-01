from sqlalchemy import (
    Column,
    Text,
    Integer,
    DateTime
    )
from geoalchemy2 import Geometry

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

schema = 'reportr'


class Point(Base):
    __tablename__ = 'points'
    __table_args__ = {'schema': schema}
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    date = Column(DateTime)
    geom = Column(Geometry('POINT', 4326))
