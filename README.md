# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, Tailwind CSS
- Backend: FastAPI
- Database: PostgreSQL, planned
- Local development: Docker Compose, planned
- Testing: pytest for backend tests
- CI/CD: GitHub Actions planned

## Monorepo Structure

```text
apps/
  api/        FastAPI backend, planned
  web/        Next.js frontend, planned
docs/         Product, roadmap, decisions, and task notes
infra/
  docker/     Local infrastructure configuration, planned
```

## Local Development Status

Milestone 1B adds a minimal FastAPI backend with a `/health` endpoint and one pytest test. Database, Docker, authentication, and frontend commands are still planned.

## Current Milestone

Current milestone: M1B - FastAPI health check and backend test setup.

## Backend Local Development

Available now:

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

## Planned Commands

These commands are planned for future milestones and are not available yet:

```bash
# Planned for M1C: frontend development server
cd apps/web
npm run dev

# Planned for M1D: Docker Compose local baseline
docker compose -f infra/docker/docker-compose.yml up
```
