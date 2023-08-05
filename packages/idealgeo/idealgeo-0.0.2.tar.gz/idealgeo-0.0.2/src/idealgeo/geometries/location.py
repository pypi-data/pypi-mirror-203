from enum import Enum

from pydantic import BaseModel

class LocationType(Enum):
    buffer = "buffer"
    region = "region"
    custom = "custom"

class Location(BaseModel):
    type: LocationType

    def __str__(self):
        return self.json()
