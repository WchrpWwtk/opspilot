# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, plain CSS for the current shell
- Backend: FastAPI, SQLAlchemy async foundation, typed model conventions, Alembic migration tooling
- Database: PostgreSQL local service, async connection foundation added, model conventions defined, application persistence planned
- Local development: Docker Compose
- Testing: pytest for backend tests
- CI/CD: GitHub Actions planned

## Monorepo Structure

```text
apps/
  api/        FastAPI backend
  web/        Next.js frontend
docs/         Product, roadmap, decisions, and task notes
compose.yml   Docker Compose local development baseline
infra/        Deployment and infrastructure configuration, planned
```

## Local Development Status

Milestone 2C adds reusable SQLAlchemy model conventions for the backend. The backend has `/health` and `/health/db` endpoints, async SQLAlchemy session setup, Alembic migration tooling, and a pytest suite that does not require Docker. Real database models, actual schema migrations, authentication, and frontend API integration are still planned.

## Current Milestone

Current milestone: M2C - SQLAlchemy Model Conventions.

## Docker Compose Local Development

Copy the non-secret local development environment template:

```bash
cp .env.example .env
```

Start Postgres, the FastAPI backend, and the Next.js frontend:

```bash
docker compose up --build
```

If an old PostgreSQL volume was already created with the previous local setup, reset the local Docker volumes before starting again:

```bash
docker compose down -v
docker compose up --build
```

In another terminal, verify the backend health check:

```bash
curl http://127.0.0.1:8000/health
```

Verify the database health check while Docker Compose is running:

```bash
curl http://127.0.0.1:8000/health/db
```

The API container uses Docker service DNS `postgres:5432` to reach PostgreSQL. Commands run from the host machine cannot use `postgres:5432`; host commands must connect through the published port at `127.0.0.1:5433`.

Open the frontend:

```bash
http://localhost:3000
```

Stop the local stack:

```bash
docker compose down
```

## Backend Local Development

Start the FastAPI backend:

```bash
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

In another terminal, verify the health check:

```bash
curl http://127.0.0.1:8000/health
```

Run backend tests:

```bash
cd apps/api
uv run pytest
```

## Backend Database Migrations

Alembic is configured under `apps/api/alembic` and reads `DATABASE_URL` from the backend settings/environment. There are no actual schema migration revisions yet.

Current model status: SQLAlchemy model conventions exist for UUID primary keys plus `created_at` and `updated_at` timestamps. No real models or database tables exist yet, and no schema migration revisions exist yet.

When Docker Compose is running, Alembic can be checked from inside the API container. This uses the container environment where PostgreSQL is reachable at `postgres:5432`:

```bash
docker compose exec api uv run alembic current
```

Alembic can also be checked from the host, but host commands must override `DATABASE_URL` to use the published PostgreSQL port at `127.0.0.1:5433`:

```bash
cd apps/api
DATABASE_URL=postgresql+asyncpg://opspilot:change_me_for_local_dev@127.0.0.1:5433/opspilot uv run alembic current
```

Create a future migration after models are added:

```bash
cd apps/api
DATABASE_URL=postgresql+asyncpg://opspilot:change_me_for_local_dev@127.0.0.1:5433/opspilot uv run alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```bash
cd apps/api
DATABASE_URL=postgresql+asyncpg://opspilot:change_me_for_local_dev@127.0.0.1:5433/opspilot uv run alembic upgrade head
```

## Frontend Local Development

Install frontend dependencies:

```bash
cd apps/web
pnpm install
```

Start the Next.js development server:

```bash
cd apps/web
pnpm dev
```

Run the frontend type check:

```bash
cd apps/web
pnpm typecheck
```

The frontend currently displays the backend health check URL as a placeholder and does not call the backend yet.
