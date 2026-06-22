# Tasks

## M1A: Documentation and Configuration Baseline

Status: Complete.

- [x] Add project overview to `README.md`
- [x] Document intended tech stack
- [x] Document monorepo structure
- [x] Mark local development commands as planned, not available
- [x] Add staged roadmap to `docs/ROADMAP.md`
- [x] Record initial architecture decisions in `docs/DECISIONS.md`
- [x] Add non-secret environment placeholders to `.env.example`
- [x] Review M1A changes
- [x] Approve moving to M1B

## M1B: FastAPI Health Check and Backend Test Setup

Status: Complete.

- [x] Create minimal backend project metadata in `apps/api/pyproject.toml`
- [x] Expose a FastAPI `app` from `apps/api/app/main.py`
- [x] Add `GET /health` returning `{"status": "ok"}`
- [x] Add one pytest test for `/health`
- [x] Update `README.md` with available backend run and test commands
- [x] Approve moving to M1C

## M1C: Frontend Shell

Status: Complete.

- [x] Create minimal Next.js frontend package in `apps/web/package.json`
- [x] Add `dev`, `build`, `start`, and `typecheck` scripts
- [x] Add App Router files in `apps/web/app`
- [x] Render the OpsPilot AI landing shell
- [x] Show current milestone as `M1C Frontend Shell`
- [x] Show backend health check URL placeholder without calling the backend
- [x] Use plain CSS in `apps/web/app/globals.css`
- [x] Update `README.md` with separate backend and frontend commands
- [x] Approve moving to M1D

## M1D: Docker Compose Local Development Baseline

Status: Complete.

- [x] Add root-level `compose.yml`
- [x] Add `postgres`, `api`, and `web` services
- [x] Use PostgreSQL 18 for the local database service
- [x] Build the API service from `apps/api`
- [x] Build the web service from `apps/web`
- [x] Expose local ports 5432, 8000, and 3000
- [x] Add a named volume for Postgres data
- [x] Add development Dockerfiles for API and web
- [x] Add API and web `.dockerignore` files
- [x] Update `.env.example` for Docker Compose local defaults
- [x] Update `README.md` with Docker Compose commands
- [x] Record root-level Compose decision in `docs/DECISIONS.md`
- [ ] Approve moving to M2
