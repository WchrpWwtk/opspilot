# Architecture Decisions

## Initial Decisions

- Use a monorepo layout with separate `apps/web`, `apps/api`, `docs`, and `infra` areas.
- Use Next.js App Router for the frontend.
- Use FastAPI for the backend API.
- Target PostgreSQL as the production database.
- Use Docker Compose for local development infrastructure.
- Use pytest for backend testing.
- Work in small milestone-based steps so each change remains reviewable.

## Docker Compose Local Development

- Keep `compose.yml` at the repository root so local development can start with `docker compose up --build` from the project root.
- Mount the PostgreSQL 18 named data volume at `/var/lib/postgresql`; PostgreSQL 18 Docker images no longer accept the old `/var/lib/postgresql/data` mount target.
- API containers should connect to PostgreSQL through Docker service DNS at `postgres:5432`.
- Host PostgreSQL access uses `POSTGRES_HOST_PORT`; the default host port is `5433`.

## Backend Database Access

- Use SQLAlchemy async for database access.
- Use `asyncpg` as the PostgreSQL driver.
- Do not create database tables automatically from application startup code.

## Backend Database Migrations

- Use Alembic for database migrations.
- Alembic reads `DATABASE_URL` from the backend settings/environment configuration.
- Keep migrations under `apps/api/alembic`.
- Do not create database tables automatically from application startup code.
