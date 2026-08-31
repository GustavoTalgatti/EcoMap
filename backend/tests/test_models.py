from app.database import Base, engine, SessionLocal
from app.models import CollectionPoint, Suggestion, User
from app.models.enums import MaterialType, PointStatus, SuggestionStatus, UserRole


def test_tables_created():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user = User(
            email="test@ecomap.dev",
            password_hash="hashed",
            name="Test User",
            role=UserRole.USER,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        point = CollectionPoint(
            name="Ponto Teste",
            latitude=-23.601,
            longitude=-46.752,
            address="Rua Teste, 100",
            material_types=[MaterialType.PLASTIC, MaterialType.PAPER],
            status=PointStatus.ACTIVE,
            created_by=user.id,
        )
        db.add(point)
        db.commit()
        db.refresh(point)

        suggestion = Suggestion(
            user_id=user.id,
            name="Sugestão Teste",
            latitude=-23.602,
            longitude=-46.753,
            address="Av. Teste, 200",
            material_types=[MaterialType.GLASS],
            status=SuggestionStatus.PENDING,
        )
        db.add(suggestion)
        db.commit()
        db.refresh(suggestion)

        assert user.id is not None
        assert point.material_types == [MaterialType.PLASTIC, MaterialType.PAPER]
        assert suggestion.status == SuggestionStatus.PENDING
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
