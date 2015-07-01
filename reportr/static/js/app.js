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

var pointSource = new ol.source.Vector({
  format: new ol.format.GeoJSON(),
  url: URL_POINTS
});
var pointLayer = new ol.layer.Vector({
  source: pointSource,
  style: new ol.style.Style({
    image: new ol.style.Icon({
      src: 'static/marker.png'
    })
  })
});
map.addLayer(pointLayer);
