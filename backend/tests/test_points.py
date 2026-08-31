from app.models import CollectionPoint
from app.models.enums import MaterialType, PointStatus


def test_list_points_returns_all_active(client, db_session):
    point = CollectionPoint(
        name="Ponto A",
        latitude=-23.601,
        longitude=-46.752,
        address="Rua A, 1",
        material_types=[MaterialType.PLASTIC.value, MaterialType.PAPER.value],
        status=PointStatus.ACTIVE,
    )
    db_session.add(point)
    db_session.commit()

    response = client.get("/api/points")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Ponto A"


def test_list_points_filters_by_material(client, db_session):
    p1 = CollectionPoint(
        name="Só Plástico",
        latitude=-23.601,
        longitude=-46.752,
        address="Rua B, 2",
        material_types=[MaterialType.PLASTIC.value],
        status=PointStatus.ACTIVE,
    )
    p2 = CollectionPoint(
        name="Só Vidro",
        latitude=-23.602,
        longitude=-46.753,
        address="Rua C, 3",
        material_types=[MaterialType.GLASS.value],
        status=PointStatus.ACTIVE,
    )
    db_session.add_all([p1, p2])
    db_session.commit()

    response = client.get("/api/points", params={"material": "plastic"})
    assert response.status_code == 200
    names = [p["name"] for p in response.json()]
    assert "Só Plástico" in names
    assert "Só Vidro" not in names


def test_get_point_by_id(client, db_session):
    point = CollectionPoint(
        name="Detalhe",
        latitude=-23.603,
        longitude=-46.754,
        address="Rua D, 4",
        material_types=[MaterialType.METAL.value],
        status=PointStatus.ACTIVE,
    )
    db_session.add(point)
    db_session.commit()
    db_session.refresh(point)

    response = client.get(f"/api/points/{point.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Detalhe"


def test_get_point_not_found(client):
    response = client.get("/api/points/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ponto não encontrado"
