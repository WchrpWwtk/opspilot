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
- Commands running from the host must connect to PostgreSQL at `127.0.0.1:5433`, not Docker service DNS `postgres:5432`.

## Backend Database Access

- Use SQLAlchemy async for database access.
- Use `asyncpg` as the PostgreSQL driver.
- Do not create database tables automatically from application startup code.

## Backend Database Migrations

- Use Alembic for database migrations.
- Alembic reads `DATABASE_URL` from the backend settings/environment configuration.
- Keep migrations under `apps/api/alembic`.
- Do not create database tables automatically from application startup code.
- Schema changes must go through Alembic migrations.
- Run Alembic inside the API container when using the container `DATABASE_URL`; host-run Alembic commands must override `DATABASE_URL` to use `127.0.0.1:5433`.

## SQLAlchemy Model Conventions

- Future database tables should use UUID primary keys.
- Future database tables should include `created_at` and `updated_at` timestamps.
- Do not create database tables automatically from application startup code.
- Schema changes must go through Alembic migrations.

## Initial User Table

- The first real database table is `users`.
- The `users` table uses a UUID primary key.
- User email addresses are required and uniquely indexed.
- User roles use simple string values in M2D: `admin`, `manager`, and `staff`.
- Role authorization will be implemented in M3, not M2D.
- Migrations, not application startup, own schema creation.
