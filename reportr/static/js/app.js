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

var newPointSource = new ol.source.Vector();
var newPointLayer = new ol.layer.Vector({
  source: newPointSource,
  style: new ol.style.Style({
    image: new ol.style.Icon({
      src: 'static/marker-new.png'
    })
  })
});
map.addLayer(newPointLayer);

var layerFilter = function(layer) {
  return layer === pointLayer;
}

// change mouse cursor when over marker
map.on('pointermove', function(e) {
  if (e.dragging) {
    return;
  }
  var pixel = map.getEventPixel(e.originalEvent);
  var hit = map.hasFeatureAtPixel(pixel, layerFilter);
  map.getTargetElement().style.cursor = hit ? 'pointer' : '';
});

var showPoint = function(feature) {
  $('#new').hide();
  $('#problem-title').text(feature.get('title'));
  var description = feature.get('description') === null ? '' : feature.get('description');
  $('#problem-description').text(description);
  $('#problem-date').text(new Date(feature.get('date')).toLocaleString());
  $('#detail').show();
};

map.on('click', function(evt) {
  newPointSource.clear();
  var feature = map.forEachFeatureAtPixel(evt.pixel,
      function(feature, layer) {
        return feature;
      }, undefined, layerFilter);
  if (feature) {
    showPoint(feature);
  } else {
    // create new
    $('#detail').hide();
    $('#new').show();
    $('#problem-title-input').val('');
    $('#problem-description-input').val('');
    newPointSource.clear();
    var newFeature = new ol.Feature(
      new ol.geom.Point(evt.coordinate)
    );
    newPointSource.addFeature(newFeature);

    $('#new-problem-form').submit(function(event) {
      event.preventDefault();

      if ($('#problem-title-input').val() == '') {
        return;
      }

      var lonLat = ol.proj.toLonLat(evt.coordinate, 'EPSG:3857');
      var title = $('#problem-title-input').val();
      var description = $('#problem-description-input').val();
      var data = {
        title: title,
        description: description,
        lon: lonLat[0],
        lat: lonLat[1]
      };

      $.post(URL_POINTS_ADD, data, function(result, status) {
        if (status === 'success') {
          newFeature.set('id', result.properties.id);
          newFeature.set('date', result.properties.date);
          newFeature.set('title', result.properties.title);
          newFeature.set('description', result.properties.description);
          newPointSource.removeFeature(newFeature);
          pointSource.addFeature(newFeature);
          showPoint(newFeature);
        }
      }, 'json');
    });
  }
});
