from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CollectionPoint
from app.models.enums import MaterialType, PointStatus
from app.schemas.point import PointRead

router = APIRouter()


@router.get("/points", response_model=list[PointRead])
def list_points(
    material: list[MaterialType] | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(CollectionPoint).filter(CollectionPoint.status == PointStatus.ACTIVE)
    points = query.all()
    if material:
        material_values = {m.value for m in material}
        points = [p for p in points if material_values.intersection(set(p.material_types))]
    return points


@router.get("/points/{point_id}", response_model=PointRead)
def get_point(point_id: int, db: Session = Depends(get_db)):
    point = db.query(CollectionPoint).filter(CollectionPoint.id == point_id).first()
    if not point:
        raise HTTPException(status_code=404, detail="Ponto não encontrado")
    return point
