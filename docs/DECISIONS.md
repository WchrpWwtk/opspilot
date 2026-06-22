# Architecture Decisions

## Initial Decisions

- Use a monorepo layout with separate `apps/web`, `apps/api`, `docs`, and `infra` areas.
- Use Next.js App Router for the frontend.
- Use FastAPI for the backend API.
- Target PostgreSQL as the production database.
- Use Docker Compose for local development infrastructure.
- Use pytest for backend testing.
- Work in small milestone-based steps so each change remains reviewable.
