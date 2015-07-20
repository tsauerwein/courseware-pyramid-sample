import unittest

from pyramid import testing

from .models import DBSession


class TestViews(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('postgresql://www-data:www-data@localhost:5432/test')
        DBSession.configure(bind=engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_points(self):
        from .views import points
        request = testing.DummyRequest()
        geojson = points(request)

        self.assertTrue(isinstance(geojson, dict))
        self.assertEqual(geojson['type'], 'FeatureCollection')

        features = geojson['type']
        self.assertTrue(len(features) > 0)
