from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import MaterialType, SuggestionStatus


class SuggestionCreate(BaseModel):
    name: str = Field(min_length=2)
    latitude: float
    longitude: float
    address: str = Field(min_length=5)
    material_types: list[MaterialType] = Field(min_length=1)
    description: str | None = None


class SuggestionReview(BaseModel):
    status: SuggestionStatus


class SuggestionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    latitude: float
    longitude: float
    address: str
    material_types: list[MaterialType]
    description: str | None
    status: SuggestionStatus
    reviewed_by: int | None
    reviewed_at: datetime | None
    created_at: datetime
