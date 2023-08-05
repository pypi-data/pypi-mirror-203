from typing import Dict

from geojson_pydantic import Feature, Polygon
from pydantic import Field

from .location import Location, LocationType


class CustomPolygon(Location):
    id: str = Field(..., description="ID of the polygon")
    type: LocationType = Field(LocationType.custom, description="Type of the location")
    geometry: Feature[Polygon, Dict] = Field(..., description="GeoJSON Feature containing a polygon and optional properties")

