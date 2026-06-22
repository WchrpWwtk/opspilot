# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, plain CSS for the current shell
- Backend: FastAPI
- Database: PostgreSQL, planned
- Local development: Docker Compose, planned
- Testing: pytest for backend tests
- CI/CD: GitHub Actions planned

## Monorepo Structure

```text
apps/
  api/        FastAPI backend
  web/        Next.js frontend
docs/         Product, roadmap, decisions, and task notes
infra/
  docker/     Local infrastructure configuration, planned
```

## Local Development Status

Milestone 1C adds a minimal Next.js frontend shell. The backend has a `/health` endpoint and one pytest test. Database, Docker, authentication, and frontend API integration are still planned.

## Current Milestone

Current milestone: M1C - Frontend Shell.

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

## Planned Commands

These commands are planned for future milestones and are not available yet:

```bash
# Planned for M1D: Docker Compose local baseline
docker compose -f infra/docker/docker-compose.yml up
```
