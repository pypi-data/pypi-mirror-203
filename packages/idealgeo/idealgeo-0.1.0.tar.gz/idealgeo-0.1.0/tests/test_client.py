import os

import pytest

from idealgeo import IdealSpotClient
from idealgeo.geometries import buffer, custom
from idealgeo.insights import Insight


API_KEY = os.environ.get('IDEALGEO_API_KEY')

@pytest.fixture
def client():
    return IdealSpotClient(API_KEY)

def test_insights(client):
    insights = client.insights()
    assert len(insights) > 0

    for ins in insights:
        assert isinstance(ins, Insight)

def test_describe_insight(client):
    insights = client.insights()
    for ins in insights:
        d = client.describe_insight(ins)
        assert d['id'] == ins.id

def test_query_insight(client):
    insights = client.insights()

    buf_ring = buffer.RingBuffer(30.264757, -97.7356077, 3)
    buf_dt = buffer.DriveTimeBuffer(30.264757, -97.7356077, 5)

    data = client.query_insight(insights[0], [buf_ring, buf_dt])

    assert len(data) > 0
    
def test_query_insight_with_opts(client):
    '''Query an insight with parameters (ancestry)'''
    insights = client.insights()

    buf_ring = buffer.RingBuffer(30.264757, -97.7356077, 3)

    data = client.query_insight(insights[2], [buf_ring], insight_opts=dict(category=[1078, 1085]))

    assert len(data) > 0

def test_fetch_geometry(client):
    buf_ring = buffer.RingBuffer(30.264757, -97.7356077, 3)
    data = client.fetch_geometry(buf_ring)
    print(data)
    assert data['type'] == 'FeatureCollection'
    assert data['features'][0]['type'] == 'Feature'
    geometry = data['features'][0]['geometry']
    assert geometry['type'] == 'Polygon'
    assert len(geometry['coordinates'][0]) > 0

def test_query_intersecting_geometries(client):
    data = client.query_intersecting_geometries(30.264757, -97.7356077)
    assert len(data) > 0

def test_post_custom_geometry(client):
    feature = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              -97.74898576124808,
              30.26623764468623
            ],
            [
              -97.74898576124808,
              30.259432672930686
            ],
            [
              -97.7385432697126,
              30.259432672930686
            ],
            [
              -97.7385432697126,
              30.26623764468623
            ],
            [
              -97.74898576124808,
              30.26623764468623
            ]
          ]
        ],
        "type": "Polygon"
      }
    } 

    poly = custom.CustomPolygon(
        id='123',
        geometry=feature)
    res = client.post_custom_polygon(poly)
    assert res.get('id')

def test_query_nearest_road_segments(client):
    data = client.query_nearest_road_segments(30.264757, -97.7356077)
    assert len(data) > 0

def test_query_traffic_counts(client):
    data = client.query_traffic_counts('429440611')
    print(data)
    assert len(data) > 0
