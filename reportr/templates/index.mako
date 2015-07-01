<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('reportr:static/pyramid-16x16.png')}">

    <title>Alchemy Scaffold for The Pyramid Web Framework</title>

    <!-- Bootstrap core CSS -->
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/ol3/3.6.0/ol.css" type="text/css">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('reportr:static/theme.css')}" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">
        <h1>reportr</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div id="map" class="map"></div>
      </div>
    </div>
  </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="//oss.maxcdn.com/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/js/bootstrap.min.js"></script>
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
  </body>
</html>
