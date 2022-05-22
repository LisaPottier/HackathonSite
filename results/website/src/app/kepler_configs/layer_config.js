const layer_config = {
  'id': 'tjrbwr',
  'type': 'grid',
  'config': {
    'dataId': 'DGFiP_facilities_accessibility',
    'label': 'DGFiP facilities accessibility',
    'color': [201, 23, 23],
    'highlightColor': [252, 242, 26, 255],
    'columns': {'lat': 'latitude', 'lng': 'longitude'},
    'isVisible': true,
    'visConfig': {
      'opacity': 0.5,
      'worldUnitSize': 10,
      'colorRange': {
        'name': 'Uber Viz Sequential 4',
        'type': 'sequential',
        'category': 'Uber',
        'colors':
            ['#E6FAFA', '#C1E5E6', '#9DD0D4', '#75BBC1', '#4BA7AF', '#00939C']
      },
      'coverage': 1,
      'sizeRange': [0, 1000],
      'percentile': [0, 100],
      'elevationPercentile': [0, 100],
      'elevationScale': 51.8,
      'enableElevationZoomFactor': true,
      'colorAggregation': 'average',
      'sizeAggregation': 'average',
      'enable3d': true
    },
    'hidden': false,
    'textLabel': [{
      'field': null,
      'color': [255, 255, 255],
      'size': 18,
      'offset': [0, 0],
      'anchor': 'start',
      'alignment': 'center'
    }]
  },
  'visualChannels': {
    'colorField': {'name': 'distance', 'type': 'real'},
    'colorScale': 'quantile',
    'sizeField': {'name': 'distance', 'type': 'real'},
    'sizeScale': 'linear'
  }
}

export default layer_config;