# EcoMap

EcoMap é um mapa interativo de pontos de coleta seletiva na região de Taboão da Serra, Osasco e Embu das Artes. Projeto open source do curso UNIFECAF — AGR.QU26/2.

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e Docker Compose
- Git

## Setup rápido (< 5 minutos)

```bash
git clone https://github.com/SEU-USUARIO/ecomap.git
cd ecomap
docker compose up --build -d
docker compose exec backend python seed.py
```

Abra:

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/docs
- Health check: http://localhost:8000/api/health

## Usuários de demonstração

| Email | Senha | Papel |
|-------|-------|-------|
| admin@ecomap.dev | admin123 | admin |
| user@ecomap.dev | user123 | user |

## Desenvolvimento local (sem Docker)

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export JWT_SECRET=dev-secret
python seed.py
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Testes

```bash
# Backend
cd backend && source .venv/bin/activate && pytest -v

# Frontend
cd frontend && npm test
```

## Funcionalidades MVP

- Mapa interativo com 15 pontos de coleta (seed)
- Filtro por tipo de material (multi-select)
- Modal com detalhes do ponto
- Cadastro e login (JWT)
- Sugestão de novos pontos (status pending)
- Aprovação de sugestões via API admin
- Guia de separação de resíduos em `/guia`

## Aprovar sugestão (admin via API)

```bash
# Login admin
TOKEN=$(curl -s -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@ecomap.dev","password":"admin123"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Listar pendentes
curl -s http://localhost:8000/api/admin/suggestions \
  -H "Authorization: Bearer $TOKEN"

# Aprovar sugestão ID 1
curl -s -X PATCH http://localhost:8000/api/admin/suggestions/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status":"approved"}'
```

## Estrutura do projeto

```
ecomap/
├── frontend/     # React + Vite + Leaflet
├── backend/      # FastAPI + SQLAlchemy
├── docs/         # Specs e planos
├── docker-compose.yml
├── README.md
└── CONTRIBUTING.md
```

## Licença

MIT — veja [LICENSE](LICENSE) (adicionar na entrega final).

## Colaboradores

Projeto desenvolvido pelo grupo UNIFECAF (7 integrantes). Professor colaborador: [@robolicar1](https://github.com/robolicar1).
