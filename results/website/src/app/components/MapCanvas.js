import './MapCanvas.css'

import KeplerGl from 'kepler.gl';
import {addDataToMap} from 'kepler.gl/actions';
import {KeplerGlSchema} from 'kepler.gl/dist/schemas';
import {keplerGlReducer} from 'kepler.gl/reducers';
import React from 'react';
import {taskMiddleware} from 'react-palm/tasks';
import {Provider, useDispatch} from 'react-redux';
import {applyMiddleware, combineReducers, createStore} from 'redux';
import useSwr from 'swr';

import IDS from '../../ids.js';
import layer_config from '../kepler_configs/layer_config.js';

const customKeplerReducer = keplerGlReducer.initialState({
  uiState: {
    activeSidePanel: null,
    currentModal: null,
  }
});

const reducers = combineReducers({
  keplerGl: customKeplerReducer,
});

const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function MapCanvas() {
    return (
        <Provider store={store}>
            <Map/>
        </Provider>
    );
}

function Map() {
  const dispatch = useDispatch();
  const { data } = useSwr("covid", async () => {
    const response = await fetch('./dataset.json'); // eslint-disable-line
    const data = await response.json(); return data;
});

React.useEffect(() => {
  if (data) {
    const dataset_1 = {
      datasets: {
        info: {
          label: 'DGFiP facilities accessibility',
          id: 'DGFiP_facilities_accessibility',
        },
        data: data
      },
      option: {
        centerMap: true,
        readOnly: true,
      },
    };
    const dataset_2 = {
      version: 'v1',
      data: {
        label: 'DGFiP facilities accessibility',
        id: 'DGFiP_facilities_accessibility',
        data: dataset_1.datasets.data,
        allData: dataset_1.datasets.data.rows,
        fields: dataset_1.datasets.data.fields,
      },
    };
    const config = {
      'version': 'v1',
      'config': {
        'visState': {
          'filters': [],
          'layers': [{
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
                'opacity': 1,
                'colorBasedOn': 'distance',
                'worldUnitSize': 10,
                'colorRange': {
                  'name': 'Uber Viz Sequential 4',
                  'type': 'sequential',
                  'category': 'Uber',
                  'colors': [
                    '#E6FAFA', '#C1E5E6', '#9DD0D4', '#75BBC1', '#4BA7AF',
                    '#00939C'
                  ]
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
          }],
          'interactionConfig': {
            'tooltip': {
              'fieldsToShow': {
                'DGFiP_facilities_accessibility':
                    [{'name': 'distance', 'format': null}]
              },
              'compareMode': false,
              'compareType': 'absolute',
              'enabled': true
            },
            'brush': {'size': 0.5, 'enabled': false},
            'geocoder': {'enabled': false},
            'coordinate': {'enabled': false}
          },
          'layerBlending': 'normal',
          'splitMaps': [],
          'animationConfig': {'currentTime': null, 'speed': 1}
        },
        'mapState': {
          'bearing': 0,
          'dragRotate': false,
          'latitude': 44.90814283852575,
          'longitude': -5.612759304869703,
          'pitch': 0,
          'zoom': 4.398639536903051,
          'isSplit': false
        },
        'mapStyle': {
          'styleType': 'dark',
          'topLayerGroups': {},
          'visibleLayerGroups': {
            'label': true,
            'road': true,
            'border': false,
            'building': true,
            'water': true,
            'land': true,
            '3d building': false
          },
          'threeDBuildingColor':
              [9.665468314072013, 17.18305478057247, 31.1442867897876],
          'mapStyles': {}
        }
      }
    };
    const mapToLoad = KeplerGlSchema.load([dataset_2], config);
    console.log(mapToLoad);
    dispatch(addDataToMap(mapToLoad));
  }
}, [dispatch, data]);

return < KeplerGl
id = 'dgfip_facilities_access'
mapboxApiAccessToken = {IDS.mapbox_token} width = {window.innerWidth} height = {
    window.innerHeight - 60} />
}