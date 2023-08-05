import os

import pytest

from idealgeo import IdealSpotClient
from idealgeo.geometries import buffer
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
    '''
    Query insight
    This endpoint will fetch the insight's data layers for a given list of locations. If an insight requires parameters, they must be included here.

    data = client.query_insight(insights[0], [buf_ring, buf_dt])
    pprint(data)
    [{'data': [['group_label', 'YR2017Q2'],
               ['Median Age', 31.0],
               ['Average Age', 31.0],
               ['Median Male Age', 31.0],
               ['Male Under 5', 6055.0],
               ['Male 5 to 14', 6126.0],
               ['Average Male Age', 31.0],
               ['Median Female Age', 30.0],
               ['Male 14 to 18', 1602.0],
               ['Average Female Age', 31.0],
               ['Male 18 to 22', 14119.0],
               ['Male 22 to 25', 2580.0],
               ['Male 25 to 30', 5554.0],
               ['Male 30 to 35', 7544.0],
               ['Male 35 to 40', 6470.0],
               ['Male 40 to 45', 4951.0],
               ['Male 45 to 50', 3746.0],
               ...
    '''
    insights = client.insights()


    buf_ring = buffer.RingBuffer(30.264757, -97.7356077, 3)
    buf_dt = buffer.DriveTimeBuffer(30.264757, -97.7356077, 5)

    data = client.query_insight(insights[0], [buf_ring, buf_dt])

    assert len(data) > 0
    
