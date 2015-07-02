<%inherit file="site.mako"/>

<%block name="title">reportr</%block>
<%block name="css">
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/ol3/3.6.0/ol.css" type="text/css">
</%block>

<div class="row">
  <div class="col-md-10">
    <div id="map" class="map"></div>
  </div>
  <div class="col-md-2">
    <h3>Report problems</h3>
    Click on the map to add a new point
    <div id="detail">
      <strong>Selected problem:</strong>
      <p id="problem-title"></p>
      <p id="problem-description"></p>
      <p id="problem-date"></p>
    </div>
    <div id="new">
      <strong>Report new problem:</strong>
      <form id="new-problem-form">
        <div class="form-group">
          <label for="problem-title-input">Title</label>
          <input type="text" class="form-control input-sm" id="problem-title-input"
            name="title" placeholder="e.g. Broken Street-light">
        </div>
        <div class="form-group">
          <label for="problem-title-description">Description</label>
          <textarea class="form-control input-sm" rows="3" id="problem-description-input"
            name="description"></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-sm" id="">Submit</button>
      </form>
    </div>
  </div>
</div>

<%block name="js">
    <script src="//cdnjs.cloudflare.com/ajax/libs/ol3/3.6.0/ol.js"></script>

    <script type="text/javascript">
    var URL_POINTS = "${request.route_url('points')}";
    var URL_POINTS_ADD = "${request.route_url('point_add')}";
    </script>
    <script src="${request.static_url('reportr:static/js/app.js')}"></script>
</%block>
