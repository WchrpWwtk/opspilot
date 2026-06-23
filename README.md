# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, plain CSS for the current shell
- Backend: FastAPI, SQLAlchemy async foundation
- Database: PostgreSQL local service, async connection foundation added, application persistence planned
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

Milestone 2A adds the smallest backend database connection foundation. The backend has `/health` and `/health/db` endpoints, async SQLAlchemy session setup, and one pytest test that does not require Docker. Database models, migrations, authentication, and frontend API integration are still planned.

## Current Milestone

Current milestone: M2A - Backend Database Connection Foundation.

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

The API container uses Docker service DNS `postgres:5432` to reach PostgreSQL. `POSTGRES_HOST_PORT=5433` is only for connecting from the host machine.

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
