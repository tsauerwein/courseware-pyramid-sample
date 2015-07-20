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

    def test_point_add_error(self):
        from .views import point_add
        from pyramid.httpexceptions import HTTPBadRequest

        request = testing.DummyRequest()
        request.POST['title'] = 'Test'
        request.POST['lon'] = ''
        request.POST['lat'] = ''

        # no lon/lat given
        self.assertRaises(HTTPBadRequest, point_add, request)

    def test_point_add_success(self):
        from .views import point_add
        from pyramid.httpexceptions import HTTPBadRequest

        request = testing.DummyRequest()
        request.POST['title'] = 'Test'
        request.POST['lon'] = '8.538265'
        request.POST['lat'] = '47.394572'

        result = point_add(request)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result['type'], 'Feature')
