def test_register_and_login(client):
    register_response = client.post(
        "/api/auth/register",
        json={"email": "novo@ecomap.dev", "password": "senha123", "name": "Novo Usuário"},
    )
    assert register_response.status_code == 201
    token = register_response.json()["access_token"]
    assert token

    login_response = client.post(
        "/api/auth/login",
        json={"email": "novo@ecomap.dev", "password": "senha123"},
    )
    assert login_response.status_code == 200
    assert login_response.json()["access_token"]

    me_response = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "novo@ecomap.dev"
    assert me_response.json()["role"] == "user"


def test_login_invalid_credentials(client):
    response = client.post(
        "/api/auth/login",
        json={"email": "naoexiste@ecomap.dev", "password": "wrong"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Email ou senha inválidos"


def test_register_duplicate_email(client):
    payload = {"email": "dup@ecomap.dev", "password": "senha123", "name": "Dup"}
    client.post("/api/auth/register", json=payload)
    response = client.post("/api/auth/register", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email já cadastrado"
