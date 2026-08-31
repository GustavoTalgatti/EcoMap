from app.auth import hash_password
from app.models import User
from app.models.enums import MaterialType, SuggestionStatus, UserRole


def _create_user(db_session, email, role=UserRole.USER):
    user = User(
        email=email,
        password_hash=hash_password("senha123"),
        name="Test",
        role=role,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def _auth_header(client, email):
    response = client.post("/api/auth/login", json={"email": email, "password": "senha123"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_suggestion(client, db_session):
    user = _create_user(db_session, "sugg@ecomap.dev")
    headers = _auth_header(client, "sugg@ecomap.dev")

    response = client.post(
        "/api/suggestions",
        headers=headers,
        json={
            "name": "Novo Ponto",
            "latitude": -23.601,
            "longitude": -46.752,
            "address": "Rua Nova, 10",
            "material_types": ["plastic", "paper"],
            "description": "Perto do mercado",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "pending"
    assert data["user_id"] == user.id


def test_admin_approves_suggestion_creates_point(client, db_session):
    user = _create_user(db_session, "user2@ecomap.dev")
    admin = _create_user(db_session, "admin2@ecomap.dev", UserRole.ADMIN)
    user_headers = _auth_header(client, "user2@ecomap.dev")
    admin_headers = _auth_header(client, "admin2@ecomap.dev")

    create_resp = client.post(
        "/api/suggestions",
        headers=user_headers,
        json={
            "name": "Ponto Aprovado",
            "latitude": -23.610,
            "longitude": -46.760,
            "address": "Av. Aprovada, 50",
            "material_types": ["glass"],
        },
    )
    suggestion_id = create_resp.json()["id"]

    approve_resp = client.patch(
        f"/api/admin/suggestions/{suggestion_id}",
        headers=admin_headers,
        json={"status": "approved"},
    )
    assert approve_resp.status_code == 200
    assert approve_resp.json()["status"] == "approved"

    points_resp = client.get("/api/points")
    names = [p["name"] for p in points_resp.json()]
    assert "Ponto Aprovado" in names


def test_non_admin_cannot_list_pending(client, db_session):
    _create_user(db_session, "regular@ecomap.dev")
    headers = _auth_header(client, "regular@ecomap.dev")

    response = client.get("/api/admin/suggestions", headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Acesso restrito a administradores"
