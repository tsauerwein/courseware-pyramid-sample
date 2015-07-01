<%inherit file="site.mako"/>

<%block name="title">reportr</%block>
<%block name="css">
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/ol3/3.6.0/ol.css" type="text/css">
</%block>

<div class="row">
  <div class="col-md-12">
    <div id="map" class="map"></div>
  </div>
</div>

<%block name="js">
    <script src="//cdnjs.cloudflare.com/ajax/libs/ol3/3.6.0/ol.js"></script>

    <script type="text/javascript">
    var points = [];
    % for point in points:
    points.push({
      title: '${point.get('title')}',
      lon: ${point.get('lon')},
      lat: ${point.get('lat')}
    });
    % endfor
    </script>
    <script src="${request.static_url('reportr:static/js/app.js')}"></script>
</%block>
