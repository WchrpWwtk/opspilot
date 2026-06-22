# OpsPilot AI

OpsPilot AI is a production-style full stack portfolio project for an internal operations workflow platform with future AI-assisted features.

The project will grow in small milestones to demonstrate real-world application engineering: authentication, role-based access control, workflow management, auditability, testing, local infrastructure, and AI-assisted operations features.

## Tech Stack

- Frontend: Next.js, TypeScript, Tailwind CSS
- Backend: FastAPI, SQLAlchemy async, Pydantic
- Database: PostgreSQL
- Local development: Docker Compose
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

Local application services are not available yet. Milestone 1A only establishes project documentation and configuration placeholders.

## Current Milestone

Current milestone: M1A - Documentation and configuration baseline.

## Planned Commands

These commands are planned for future milestones and are not available yet:

```bash
# Planned for M1B: backend health check and tests
cd apps/api
pytest

# Planned for M1C: frontend development server
cd apps/web
npm run dev

# Planned for M1D: Docker Compose local baseline
docker compose -f infra/docker/docker-compose.yml up
```
