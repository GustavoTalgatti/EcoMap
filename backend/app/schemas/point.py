from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import MaterialType, PointStatus


class PointRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    latitude: float
    longitude: float
    address: str
    description: str | None
    material_types: list[MaterialType]
    opening_hours: str | None
    status: PointStatus
    created_by: int | None
    created_at: datetime
