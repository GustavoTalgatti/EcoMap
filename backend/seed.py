from passlib.context import CryptContext

from app.database import Base, SessionLocal, engine
from app.models import CollectionPoint, User
from app.models.enums import MaterialType, PointStatus, UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SEED_POINTS = [
    {
        "name": "Ecoponto Taboão Centro",
        "latitude": -23.6015,
        "longitude": -46.7523,
        "address": "Rua do Manifesto, 1000, Taboão da Serra",
        "description": "Coleta seletiva no centro da cidade.",
        "material_types": [MaterialType.PLASTIC, MaterialType.PAPER, MaterialType.METAL],
        "opening_hours": "Seg-Sex 8h-18h",
    },
    {
        "name": "Ponto Verde Jardim Maria Rosa",
        "latitude": -23.6120,
        "longitude": -46.7680,
        "address": "Av. Pirajussara, 500, Taboão da Serra",
        "description": "Container para plástico e vidro.",
        "material_types": [MaterialType.PLASTIC, MaterialType.GLASS],
        "opening_hours": "Seg-Sáb 7h-19h",
    },
    {
        "name": "Recicla Taboão Parque Pinheiros",
        "latitude": -23.5950,
        "longitude": -46.7410,
        "address": "Estrada Kizaemon Takeuti, 1200, Taboão da Serra",
        "description": "Ponto comunitário de reciclagem.",
        "material_types": [MaterialType.PAPER, MaterialType.METAL],
        "opening_hours": "Ter-Dom 9h-17h",
    },
    {
        "name": "Ecoponto Osasco Centro",
        "latitude": -23.5320,
        "longitude": -46.7910,
        "address": "Praça da Feira, 50, Osasco",
        "description": "Coleta de eletrônicos e metais.",
        "material_types": [MaterialType.ELECTRONICS, MaterialType.METAL],
        "opening_hours": "Seg-Sex 8h-17h",
    },
    {
        "name": "Ponto Azul Osasco Vila Yara",
        "latitude": -23.5450,
        "longitude": -46.7780,
        "address": "Av. dos Autonomistas, 3200, Osasco",
        "description": "Vidro e plástico.",
        "material_types": [MaterialType.GLASS, MaterialType.PLASTIC],
        "opening_hours": "Seg-Sáb 8h-18h",
    },
    {
        "name": "Recicla Osasco Presidente Altino",
        "latitude": -23.5580,
        "longitude": -46.8050,
        "address": "Rua Dona Primitiva Vianco, 200, Osasco",
        "description": "Papel e papelão.",
        "material_types": [MaterialType.PAPER],
        "opening_hours": "Seg-Sex 7h-16h",
    },
    {
        "name": "Ecoponto Embu das Artes Centro",
        "latitude": -23.6490,
        "longitude": -46.8520,
        "address": "Rua Rodrigues Alves, 150, Embu das Artes",
        "description": "Coleta orgânica e recicláveis.",
        "material_types": [MaterialType.ORGANIC, MaterialType.PLASTIC, MaterialType.PAPER],
        "opening_hours": "Seg-Sáb 8h-18h",
    },
    {
        "name": "Ponto Verde Embu Cercado Grande",
        "latitude": -23.6380,
        "longitude": -46.8350,
        "address": "Estrada de Itapecerica, 800, Embu das Artes",
        "description": "Metals e plásticos.",
        "material_types": [MaterialType.METAL, MaterialType.PLASTIC],
        "opening_hours": "Ter-Sáb 9h-17h",
    },
    {
        "name": "Coleta de Óleo Taboão Jardim Record",
        "latitude": -23.6080,
        "longitude": -46.7590,
        "address": "Rua José Bonifácio, 300, Taboão da Serra",
        "description": "Ponto exclusivo para óleo de cozinha usado.",
        "material_types": [MaterialType.OIL],
        "opening_hours": "Qua-Sáb 10h-16h",
    },
    {
        "name": "Eletrônicos Taboão Parque Assunção",
        "latitude": -23.6170,
        "longitude": -46.7450,
        "address": "Av. Intercontinental, 600, Taboão da Serra",
        "description": "Descarte de eletrônicos e pilhas.",
        "material_types": [MaterialType.ELECTRONICS],
        "opening_hours": "Seg-Sex 9h-17h",
    },
    {
        "name": "Ecoponto Taboão Jardim das Oliveiras",
        "latitude": -23.5900,
        "longitude": -46.7650,
        "address": "Rua Amazonas, 450, Taboão da Serra",
        "description": "Plástico, vidro e metal.",
        "material_types": [MaterialType.PLASTIC, MaterialType.GLASS, MaterialType.METAL],
        "opening_hours": "Seg-Dom 7h-20h",
    },
    {
        "name": "Recicla Osasco Rochdale",
        "latitude": -23.5250,
        "longitude": -46.7700,
        "address": "Av. Rochdale, 900, Osasco",
        "description": "Papel e plástico.",
        "material_types": [MaterialType.PAPER, MaterialType.PLASTIC],
        "opening_hours": "Seg-Sex 8h-18h",
    },
    {
        "name": "Ponto Orgânico Embu Parque Francisco",
        "latitude": -23.6550,
        "longitude": -46.8600,
        "address": "Rua Francisco Pereira, 80, Embu das Artes",
        "description": "Compostagem de resíduos orgânicos.",
        "material_types": [MaterialType.ORGANIC],
        "opening_hours": "Seg-Sáb 6h-14h",
    },
    {
        "name": "Coleta Mista Taboão Jardim São Judas",
        "latitude": -23.6050,
        "longitude": -46.7780,
        "address": "Rua São Judas Tadeu, 220, Taboão da Serra",
        "description": "Todos os recicláveis secos.",
        "material_types": [
            MaterialType.PLASTIC,
            MaterialType.GLASS,
            MaterialType.METAL,
            MaterialType.PAPER,
        ],
        "opening_hours": "Seg-Sex 8h-18h",
    },
    {
        "name": "Ecoponto Osasco Veloso",
        "latitude": -23.5400,
        "longitude": -46.7950,
        "address": "Av. João de Góes, 1100, Osasco",
        "description": "Vidro, metal e eletrônicos.",
        "material_types": [MaterialType.GLASS, MaterialType.METAL, MaterialType.ELECTRONICS],
        "opening_hours": "Ter-Sáb 9h-17h",
    },
]


def seed():
    db = SessionLocal()
    try:
        if db.query(User).count() > 0:
            print("Database already seeded, skipping.")
            return

        admin = User(
            email="admin@ecomap.dev",
            password_hash=pwd_context.hash("admin123"),
            name="Admin EcoMap",
            role=UserRole.ADMIN,
        )
        user = User(
            email="user@ecomap.dev",
            password_hash=pwd_context.hash("user123"),
            name="Usuário Demo",
            role=UserRole.USER,
        )
        db.add_all([admin, user])
        db.commit()
        db.refresh(admin)

        for data in SEED_POINTS:
            point = CollectionPoint(
                name=data["name"],
                latitude=data["latitude"],
                longitude=data["longitude"],
                address=data["address"],
                description=data["description"],
                material_types=[m.value for m in data["material_types"]],
                opening_hours=data["opening_hours"],
                status=PointStatus.ACTIVE,
                created_by=admin.id,
            )
            db.add(point)

        db.commit()
        print(f"Seeded {len(SEED_POINTS)} collection points and 2 users.")
    finally:
        db.close()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    seed()
