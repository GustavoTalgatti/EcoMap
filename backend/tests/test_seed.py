from app.database import Base, SessionLocal, engine
from app.models import CollectionPoint, User
from app.models.enums import UserRole
from seed import seed


def test_seed_creates_users_and_points():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seed()
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.email == "admin@ecomap.dev").first()
        user = db.query(User).filter(User.email == "user@ecomap.dev").first()
        points = db.query(CollectionPoint).all()
        assert admin is not None
        assert admin.role == UserRole.ADMIN
        assert user is not None
        assert user.role == UserRole.USER
        assert len(points) == 15
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
