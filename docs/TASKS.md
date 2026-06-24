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
- [x] Approve moving to M2

## M2A: Backend Database Connection Foundation

Status: Complete.

- [x] Add `sqlalchemy`, `asyncpg`, and `pydantic-settings` backend dependencies
- [x] Add backend settings for `APP_ENV`, `DATABASE_URL`, and `CORS_ALLOWED_ORIGINS`
- [x] Add async SQLAlchemy engine and session factory
- [x] Add `get_db_session` dependency
- [x] Avoid automatic table creation
- [x] Keep `GET /health` returning `{"status": "ok"}`
- [x] Add `GET /health/db` database reachability check
- [x] Fix PostgreSQL 18 local volume mount target
- [x] Keep default backend tests independent of Docker and live PostgreSQL
- [x] Document backend test and Docker health-check commands
- [x] Approve moving to M2B

## M2B: Alembic Migration Baseline

Status: Complete.

- [x] Add `alembic` as the only new backend production dependency
- [x] Add SQLAlchemy declarative base without defining models
- [x] Add backend Alembic configuration under `apps/api`
- [x] Load Alembic database URL from backend settings/environment
- [x] Configure Alembic for async SQLAlchemy PostgreSQL URLs
- [x] Track an empty `alembic/versions` directory with `.gitkeep`
- [x] Avoid creating real migration revisions or database tables
- [x] Document backend migration commands in `README.md`
- [x] Record migration decisions in `docs/DECISIONS.md`
- [x] Approve moving to M2C

## M2C: SQLAlchemy Model Conventions

Status: Complete.

- [x] Keep a single SQLAlchemy declarative `Base` for Alembic target metadata
- [x] Add an abstract UUID primary key convention
- [x] Add abstract timezone-aware `created_at` and `updated_at` timestamp conventions
- [x] Use database-side timestamp defaults where appropriate
- [x] Avoid defining concrete models, table names, database tables, or migration revisions
- [x] Add tests for base metadata and shared conventions without requiring PostgreSQL or Docker
- [x] Update `README.md` with current model status
- [x] Record model and migration decisions in `docs/DECISIONS.md`
- [x] Approve moving to M2D

## M2D: Initial User Model and Migration

Status: Complete.

- [x] Add initial `User` SQLAlchemy model
- [x] Use the existing UUID primary key and timestamp conventions
- [x] Add required `email`, `full_name`, `role`, and `is_active` fields
- [x] Use simple role values: `admin`, `manager`, and `staff`
- [x] Keep login, password hashing, sessions, JWTs, and API routes out of M2D
- [x] Explicitly import the User model for Alembic metadata discovery
- [x] Add one Alembic revision that creates and drops the `users` table
- [x] Uniquely index `users.email`
- [x] Add model metadata tests that do not require PostgreSQL or Docker
- [x] Update migration instructions in `README.md`
- [x] Record M2D decisions in `docs/DECISIONS.md`
- [ ] Approve moving to M3
