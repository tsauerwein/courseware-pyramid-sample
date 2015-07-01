var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.MapQuest({layer: 'osm'})
    })
  ],
  controls: ol.control.defaults({
    attributionOptions: {
      collapsible: false
    }
  }),
  target: 'map',
  view: new ol.View({
    center: ol.proj.fromLonLat([8.531267, 47.386665], 'EPSG:3857'),
    zoom: 13
  })
});

if (points !== undefined) {
  var pointSource = new ol.source.Vector();
  var pointLayer = new ol.layer.Vector({
    source: pointSource,
    style: new ol.style.Style({
      image: new ol.style.Icon({
        src: 'static/marker.png'
      })
    })
  });
  map.addLayer(pointLayer);

  for(var i = 0; i < points.length; i++) {
    var point = points[i];
    var feature = new ol.Feature({
      title: point.title,
      geometry: new ol.geom.Point(
        ol.proj.fromLonLat([point.lon, point.lat], 'EPSG:3857'))
    });
    pointSource.addFeature(feature);
  }
}
