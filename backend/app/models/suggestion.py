from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import SuggestionStatus


class Suggestion(Base):
    __tablename__ = "suggestions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    material_types: Mapped[list] = mapped_column(JSON, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[SuggestionStatus] = mapped_column(
        Enum(SuggestionStatus), default=SuggestionStatus.PENDING, nullable=False
    )
    reviewed_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="suggestions", foreign_keys=[user_id])
