from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Suggestion, User
from app.models.enums import SuggestionStatus
from app.schemas.suggestion import SuggestionCreate, SuggestionRead

router = APIRouter(prefix="/suggestions", tags=["suggestions"])


@router.post("", response_model=SuggestionRead, status_code=status.HTTP_201_CREATED)
def create_suggestion(
    payload: SuggestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    suggestion = Suggestion(
        user_id=current_user.id,
        name=payload.name,
        latitude=payload.latitude,
        longitude=payload.longitude,
        address=payload.address,
        material_types=[m.value for m in payload.material_types],
        description=payload.description,
        status=SuggestionStatus.PENDING,
    )
    db.add(suggestion)
    db.commit()
    db.refresh(suggestion)
    return suggestion


@router.get("/mine", response_model=list[SuggestionRead])
def my_suggestions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Suggestion)
        .filter(Suggestion.user_id == current_user.id)
        .order_by(Suggestion.created_at.desc())
        .all()
    )
