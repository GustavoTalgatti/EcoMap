# EcoMap — Design Specification

**Date:** 2026-08-31  
**Course:** UNIFECAF — Open Source Contribution & Collaboration (AGR.QU26/2)  
**Theme:** Sustentabilidade  
**Status:** Approved

## Overview

EcoMap is a web application that displays recycling collection points on an interactive map. Users can filter points by material type, suggest new locations, and read a guide on waste separation. The system is designed for a 7-person student group with GitHub-based open source collaboration.

## Goals

- Deliver a simple, demonstrable MVP for the course
- Enable parallel development across 7 contributors via clear module boundaries
- Version control on GitHub with the professor (`robolicar1`) as collaborator
- Provide README and CONTRIBUTING docs for onboarding new contributors

## Non-Goals (MVP)

- Native mobile app
- Paid map APIs (Google Maps)
- Microservices architecture
- Star ratings and collection reminders (deferred to Phase 2)
- Complex CI/CD pipeline

## Architecture

Monorepo with two applications:

| Layer | Technology | Port |
|-------|-----------|------|
| Frontend | React 18 + Vite + TypeScript + Leaflet | 5173 |
| Backend | FastAPI + SQLAlchemy + Pydantic | 8000 |
| Database | SQLite (`ecomap.db`) | — |
| Maps | Leaflet.js + OpenStreetMap tiles | — |
| Auth | JWT (email + password, HS256) | — |

```
Frontend (React) ──REST JSON──▶ Backend (FastAPI) ──▶ SQLite
```

## Data Model

### User

| Field | Type | Notes |
|-------|------|-------|
| id | int PK | auto |
| email | str unique | login identifier |
| password_hash | str | bcrypt |
| name | str | display name |
| role | enum | `user` \| `admin` |
| created_at | datetime | auto |

### CollectionPoint

| Field | Type | Notes |
|-------|------|-------|
| id | int PK | auto |
| name | str | point name |
| latitude | float | WGS84 |
| longitude | float | WGS84 |
| address | str | street address |
| description | str nullable | extra info |
| material_types | JSON array | values from MaterialType enum |
| opening_hours | str nullable | e.g. "Mon-Fri 8h-18h" |
| status | enum | `active` \| `inactive` |
| created_by | int FK nullable | user who created |
| created_at | datetime | auto |

### Suggestion

| Field | Type | Notes |
|-------|------|-------|
| id | int PK | auto |
| user_id | int FK | submitter |
| name | str | proposed name |
| latitude | float | WGS84 |
| longitude | float | WGS84 |
| address | str | street address |
| material_types | JSON array | values from MaterialType enum |
| description | str nullable | extra info |
| status | enum | `pending` \| `approved` \| `rejected` |
| reviewed_by | int FK nullable | admin who reviewed |
| reviewed_at | datetime nullable | review timestamp |
| created_at | datetime | auto |

### MaterialType (enum)

`plastic` | `glass` | `metal` | `paper` | `electronics` | `oil` | `organic`

Labels (PT-BR): Plástico, Vidro, Metal, Papel, Eletrônicos, Óleo, Orgânico

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/health` | — | Health check |
| GET | `/api/points` | — | List points; query param `material` filters |
| GET | `/api/points/{id}` | — | Point detail |
| POST | `/api/auth/register` | — | Create account |
| POST | `/api/auth/login` | — | Returns JWT |
| GET | `/api/auth/me` | JWT | Current user |
| POST | `/api/suggestions` | JWT | Submit new point suggestion |
| GET | `/api/suggestions/mine` | JWT | User's suggestions |
| GET | `/api/admin/suggestions` | JWT admin | List pending suggestions |
| PATCH | `/api/admin/suggestions/{id}` | JWT admin | Approve or reject |

## Frontend Pages

| Route | Component | Description |
|-------|-----------|-------------|
| `/` | MapPage | Map + filter bar + point markers |
| `/guia` | GuidePage | Static waste separation guide |
| `/login` | LoginPage | Email/password login |
| `/register` | RegisterPage | Account creation |
| `/sugerir` | SuggestPage | Form to propose new point (auth required) |

## MVP Features

1. Interactive map with collection point markers (≥ 10 seed points)
2. Filter by material type (multi-select chips)
3. Point detail modal (name, address, materials, hours)
4. User registration and login (JWT)
5. Authenticated users can suggest new points (status: pending)
6. Admin can approve suggestions via API (creates CollectionPoint)
7. Static guide page explaining waste separation
8. README with setup instructions (< 5 minutes)
9. CONTRIBUTING.md with PR workflow

## Phase 2 (Post-MVP)

- Star ratings on collection points
- Collection day reminders (in-app or email)
- Admin UI panel for suggestion approval

## Team Division (7 people)

| Person | Module | Branch |
|--------|--------|--------|
| 1 | Monorepo setup, Docker Compose, README | `chore/setup` |
| 2 | Backend models, migrations, seed | `feat/backend-models` |
| 3 | Backend API points + filters | `feat/api-points` |
| 4 | Backend auth JWT + suggestions | `feat/api-auth-suggestions` |
| 5 | Frontend map (Leaflet) + markers | `feat/frontend-map` |
| 6 | Frontend filters, modal, guide page | `feat/frontend-ui` |
| 7 | Tests + CONTRIBUTING.md | `feat/tests-docs` |

## Git Workflow

- `main` branch protected; merges via PR only
- Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`
- PR template with checklist in `.github/PULL_REQUEST_TEMPLATE.md`
- Professor GitHub: `robolicar1` (email: robolicar@gmail.com)

## Acceptance Criteria

- [ ] GitHub repo with commit history from all group members
- [ ] Professor added as collaborator
- [ ] `docker compose up` starts frontend and backend
- [ ] Map loads with ≥ 10 seed points in Taboão da Serra / Grande SP area
- [ ] Material filter returns correct subset of points
- [ ] Login + suggestion saves to database with status `pending`
- [ ] Guide page accessible at `/guia`
- [ ] Backend tests pass (`pytest`)
- [ ] Demo presentable in ~3 minutes

## Repository Structure

```
ecomap/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   ├── package.json
│   └── vite.config.ts
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── auth.py
│   │   ├── database.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── seed.py
├── docs/
│   └── superpowers/
├── docker-compose.yml
├── README.md
├── CONTRIBUTING.md
└── .github/
    └── PULL_REQUEST_TEMPLATE.md
```

## Seed Data

15 collection points in the Taboão da Serra / Osasco / Embu das Artes region with varied material types. One admin user (`admin@ecomap.dev` / `admin123`) and one regular user (`user@ecomap.dev` / `user123`) for demo.

## Error Handling

- API returns JSON `{ "detail": "message" }` with appropriate HTTP status codes
- Frontend shows toast/alert on API errors
- Form validation on both client (required fields) and server (Pydantic)

## Security

- Passwords hashed with bcrypt
- JWT secret from environment variable (`JWT_SECRET`)
- CORS restricted to frontend origin in production
- Admin endpoints require `role=admin`

## Testing Strategy

| Layer | Tool | Coverage |
|-------|------|----------|
| Backend unit/integration | pytest + httpx | Points CRUD, filters, auth, suggestions |
| Frontend components | Vitest + Testing Library | FilterBar, material chip toggle |
| Manual | README checklist | End-to-end smoke test |
