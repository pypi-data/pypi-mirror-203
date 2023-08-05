from pydantic import BaseModel, Field


class Insight(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    version: str = Field(...)
    description: str = Field(...)

    def __repr__(self):
        return 'Insight<{}, {}>'.format(self.id, self.version)

