from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import get_current_admin
from app.database import get_db
from app.models import CollectionPoint, Suggestion, User
from app.models.enums import PointStatus, SuggestionStatus
from app.schemas.suggestion import SuggestionRead, SuggestionReview

router = APIRouter(prefix="/admin/suggestions", tags=["admin"])


@router.get("", response_model=list[SuggestionRead])
def list_pending_suggestions(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return (
        db.query(Suggestion)
        .filter(Suggestion.status == SuggestionStatus.PENDING)
        .order_by(Suggestion.created_at.asc())
        .all()
    )


@router.patch("/{suggestion_id}", response_model=SuggestionRead)
def review_suggestion(
    suggestion_id: int,
    payload: SuggestionReview,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    if payload.status not in (SuggestionStatus.APPROVED, SuggestionStatus.REJECTED):
        raise HTTPException(status_code=400, detail="Status deve ser approved ou rejected")

    suggestion = db.query(Suggestion).filter(Suggestion.id == suggestion_id).first()
    if not suggestion:
        raise HTTPException(status_code=404, detail="Sugestão não encontrada")
    if suggestion.status != SuggestionStatus.PENDING:
        raise HTTPException(status_code=400, detail="Sugestão já foi revisada")

    suggestion.status = payload.status
    suggestion.reviewed_by = current_admin.id
    suggestion.reviewed_at = datetime.now(timezone.utc)

    if payload.status == SuggestionStatus.APPROVED:
        point = CollectionPoint(
            name=suggestion.name,
            latitude=suggestion.latitude,
            longitude=suggestion.longitude,
            address=suggestion.address,
            description=suggestion.description,
            material_types=suggestion.material_types,
            status=PointStatus.ACTIVE,
            created_by=suggestion.user_id,
        )
        db.add(point)

    db.commit()
    db.refresh(suggestion)
    return suggestion
