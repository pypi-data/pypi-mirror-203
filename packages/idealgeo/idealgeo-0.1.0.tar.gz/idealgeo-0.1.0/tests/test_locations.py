import json

import pytest

from idealgeo.geometries import location, buffer, region, custom

def test_ring_buffer():
    assert buffer.RingBuffer(1, 2, 3).dict() == {
        'latitude': 1.0,
        'longitude': 2.0,
        'type': location.LocationType.buffer,
        'areatype': buffer.AreaTypeEnum.ring,
        'radius': 3.0,
        'units': 'miles'
    }

def test_drivetime_buffer():
    assert buffer.DriveTimeBuffer(1, 2, 3).dict() == {
        'latitude': 1.0,
        'longitude': 2.0,
        'type': location.LocationType.buffer,
        'areatype': buffer.AreaTypeEnum.drivetime,
        'radius': 3.0,
        'units': 'minutes'
    }

def test_walktime_buffer():
    assert buffer.WalkTimeBuffer(1, 2, 3).dict() == {
        'latitude': 1.0,
        'longitude': 2.0,
        'type': location.LocationType.buffer,
        'areatype': buffer.AreaTypeEnum.walktime,
        'radius': 3.0,
        'units': 'minutes'
    }

def test_biketime_buffer():
    assert buffer.BikeTimeBuffer(1, 2, 3).dict() == {
        'latitude': 1.0,
        'longitude': 2.0,
        'type': location.LocationType.buffer,
        'areatype': buffer.AreaTypeEnum.biketime,
        'radius': 3.0,
        'units': 'minutes'
    }

def test_transit_time_buffer():
    assert buffer.TransitTimeBuffer(1, 2, 3).dict() == {
        'latitude': 1.0,
        'longitude': 2.0,
        'type': location.LocationType.buffer,
        'areatype': buffer.AreaTypeEnum.transittime,
        'radius': 3.0,
        'units': 'minutes'
    }

def test_region():
    assert region.Region(region_id='123', regiontype=region.RegionEnum.nation).dict() == {
        'region_id': '123',
        'regiontype': region.RegionEnum.nation,
        'type': location.LocationType.region,
    }

def test_custom_polygon():
    gj_polygon = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [13.38272, 52.46385],
                    [13.42786, 52.46385],
                    [13.42786, 52.48445],
                    [13.38272, 52.48445],
                    [13.38272, 52.46385],
                ]
            ],
        },
        "properties": {
            "name": "bob1",
        },
    }

    gj_point = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [13.38272, 52.46385],
        },
        "properties": {
            "name": "bob2",
        },
    }

    custom_polygon = custom.CustomPolygon(id='123', geometry=gj_polygon)
    assert custom_polygon.dict()['id'] == '123'
    assert custom_polygon.dict()['type'] == location.LocationType.custom

    assert json.loads(str(custom_polygon))

    with pytest.raises(ValueError):
        custom.CustomPolygon(id='123', geometry=gj_point)


