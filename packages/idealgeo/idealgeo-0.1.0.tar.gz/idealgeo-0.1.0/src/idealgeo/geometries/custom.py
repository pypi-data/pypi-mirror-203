import json
from typing import Dict

from geojson_pydantic import Feature, Polygon
from pydantic import Field

from .location import Location, LocationType


class CustomPolygon(Location):
    id: str = Field(..., description="ID of the polygon")
    type: LocationType = Field(LocationType.custom, description="Type of the location")
    geometry: Feature[Polygon, Dict] = Field(..., description="GeoJSON Feature containing a polygon and optional properties")

    def __str__(self):
        return json.dumps({'id': self.id, 'type': self.type.value})
