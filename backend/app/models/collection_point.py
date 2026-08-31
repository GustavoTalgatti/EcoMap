from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import PointStatus


class CollectionPoint(Base):
    __tablename__ = "collection_points"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    material_types: Mapped[list] = mapped_column(JSON, nullable=False)
    opening_hours: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[PointStatus] = mapped_column(Enum(PointStatus), default=PointStatus.ACTIVE, nullable=False)
    created_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", back_populates="collection_points")
