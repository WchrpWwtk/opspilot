# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, plain CSS for the current shell
- Backend: FastAPI
- Database: PostgreSQL local service, application persistence planned
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

Milestone 1D adds a minimal Docker Compose local development baseline. The backend has a `/health` endpoint and one pytest test. Database application code, authentication, and frontend API integration are still planned.

## Current Milestone

Current milestone: M1D - Docker Compose Local Development Baseline.

## Docker Compose Local Development

Copy the non-secret local development environment template:

```bash
cp .env.example .env
```

Start Postgres, the FastAPI backend, and the Next.js frontend:

```bash
docker compose up --build
```

In another terminal, verify the backend health check:

```bash
curl http://127.0.0.1:8000/health
```

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
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
uvicorn app.main:app --reload
```

In another terminal, verify the health check:

```bash
curl http://127.0.0.1:8000/health
```

Run backend tests:

```bash
cd apps/api
pytest
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
