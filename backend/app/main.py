from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import CollectionPoint, Suggestion, User  # noqa: F401
from app.routers import admin, auth, health, points, suggestions


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="EcoMap API", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(points.router, prefix="/api", tags=["points"])
app.include_router(auth.router, prefix="/api")
app.include_router(suggestions.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
