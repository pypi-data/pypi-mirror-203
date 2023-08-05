from enum import Enum
from typing import Any, Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field, Json

from .location import Location, LocationType

class RegionEnum(str, Enum):
    nation = 'nation'
    state = 'state'
    county = 'county'
    cbsa = 'cbsa'
    city = 'city'
    place = 'place'
    tract = 'tract'
    zipcode = 'zipcode'
    blockgroup = 'blockgroup'


class Region(Location):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(..., description="Region type")
    type: LocationType = Field(LocationType.region, description="Location type")


class Nation(Region):
    region_id: str = Field('us', description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.nation, description="Region type")
   

class State(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.state, description="Region type")


class County(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.county, description="Region type")


class Cbsa(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.cbsa, description="Region type")


class City(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.city, description="Region type")


class Place(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.place, description="Region type")


class Tract(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.tract, description="Region type")


class Zipcode(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.zipcode, description="Region type")


class Blockgroup(Region):
    region_id: str = Field(..., description="Region ID")
    regiontype: RegionEnum = Field(RegionEnum.blockgroup, description="Region type")

