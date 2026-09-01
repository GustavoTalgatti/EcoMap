# Contribuindo com o EcoMap

Obrigado por contribuir! Este guia descreve o fluxo de trabalho para o grupo de 7 integrantes e colaboradores externos.

## Antes de começar

1. Leia o [README.md](README.md) e rode o projeto localmente
2. Leia a spec em `docs/superpowers/specs/2026-08-31-ecomap-design.md`
3. Escolha uma issue ou combine com o grupo quem trabalha em quê

## Divisão sugerida por módulo

| Módulo | Branch sugerida |
|--------|-----------------|
| Setup / Docker / README | `chore/setup` |
| Models + seed | `feat/backend-models` |
| API points + filtros | `feat/api-points` |
| Auth JWT + suggestions | `feat/api-auth-suggestions` |
| Mapa Leaflet | `feat/frontend-map` |
| Filtros, modal, guia | `feat/frontend-ui` |
| Testes + docs | `feat/tests-docs` |

## Fluxo Git

1. Atualize `main`: `git checkout main && git pull origin main`
2. Crie branch: `git checkout -b feat/minha-feature`
3. Faça commits pequenos com [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` nova funcionalidade
   - `fix:` correção de bug
   - `docs:` documentação
   - `test:` testes
   - `chore:` setup, deps, config
4. Rode testes antes do PR:
   ```bash
   cd backend && pytest -v
   cd ../frontend && npm test
   ```
5. Push: `git push -u origin feat/minha-feature`
6. Abra Pull Request para `main`

## Regras de PR

- PRs pequenos e focados (1 módulo por PR quando possível)
- Pelo menos 1 review de outro integrante antes do merge
- `main` é protegida — merge somente via PR
- Resolva conflitos na sua branch antes de pedir review
- Não commite `.env`, `*.db`, `node_modules/`, ou `.venv/`

## Checklist do autor

- [ ] Testes passam (`pytest` e `npm test`)
- [ ] Código segue a estrutura do monorepo
- [ ] Mensagens de erro em português (PT-BR) no frontend
- [ ] API retorna `{ "detail": "..." }` em erros
- [ ] Sem secrets no código

## Como testar manualmente

1. `docker compose up --build -d && docker compose exec backend python seed.py`
2. Abra http://localhost:5173 — mapa com ≥ 10 marcadores
3. Filtre por "Plástico" — subset correto aparece
4. Clique em marcador — modal com detalhes
5. Login em `/login` com `user@ecomap.dev` / `user123`
6. Envie sugestão em `/sugerir`
7. Aprove via API admin (ver README)
8. Acesse `/guia` — guia de separação carrega

## Dúvidas

Abra uma issue no GitHub ou combine no grupo. Professor colaborador: [@robolicar1](https://github.com/robolicar1) (robolicar@gmail.com).
