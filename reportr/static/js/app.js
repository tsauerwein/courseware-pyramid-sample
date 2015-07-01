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
    center: ol.proj.fromLonLat([6.1117, 47.80587], 'EPSG:3857'),
    zoom: 6
  })
});
