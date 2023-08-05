from enum import Enum

from pydantic import Field

from .location import Location


class AreaTypeEnum(str, Enum):
    ring = 'ring'
    drivetime = 'drivetime'
    walktime = 'walktime'
    biketime = 'biketime'
    transittime = 'transittime'


class Buffer(Location):
    latitude: float = Field(..., description="Latitude of the center of the buffer")
    longitude: float = Field(..., description="Longitude of the center of the buffer")
    areatype: AreaTypeEnum = Field(..., description="Type of area to buffer around the center point")
    radius: float = Field(..., description="Radius of the buffer")
    units: str = Field(..., description="Units of the radius")

    def __init__(self, **kwargs):
        super().__init__(type='buffer', **kwargs)


class RingBuffer(Buffer):
    def __init__(self, latitude, longitude, radius, units='miles'):
        super(RingBuffer, self).__init__(latitude=latitude, longitude=longitude, areatype='ring', radius=radius, units=units)


class DriveTimeBuffer(Buffer):
    def __init__(self, latitude, longitude, radius, units='minutes'):
        super(DriveTimeBuffer, self).__init__(latitude=latitude, longitude=longitude, areatype='drivetime', radius=radius, units=units)


class WalkTimeBuffer(Buffer):
    def __init__(self, latitude, longitude, radius, units='minutes'):
        super(WalkTimeBuffer, self).__init__(latitude=latitude, longitude=longitude, areatype='walktime', radius=radius, units=units)


class BikeTimeBuffer(Buffer):
    def __init__(self, latitude, longitude, radius, units='minutes'):
        super(BikeTimeBuffer, self).__init__(latitude=latitude, longitude=longitude, areatype='biketime', radius=radius, units=units)


class TransitTimeBuffer(Buffer):
    def __init__(self, latitude, longitude, radius, units='minutes'):
        super(TransitTimeBuffer, self).__init__(latitude=latitude, longitude=longitude, areatype='transittime', radius=radius, units=units)

