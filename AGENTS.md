# AGENTS.md

## Project

This repository is `OpsPilot AI`, a production-style portfolio project for an internal operations workflow platform.

The goal is to demonstrate real-world full stack engineering skills:

* Next.js frontend
* FastAPI backend
* PostgreSQL database
* Docker-based local development
* Authentication and authorization
* Audit logs
* Testing
* CI/CD readiness
* AI-assisted workflow features such as summarization, classification, and semantic search

## Working Agreements

* Do not implement large features in one pass.
* Before coding, summarize the task and propose a short implementation plan.
* Prefer small, reviewable diffs.
* Ask before adding new production dependencies.
* Do not create or modify secrets.
* Do not put API keys, passwords, tokens, or private credentials in code.
* Keep `.env.example` updated when adding environment variables.
* After modifying code, run the relevant checks when possible.
* If checks cannot be run, clearly explain why.

## Repository Structure

* `apps/web` — Next.js frontend
* `apps/api` — FastAPI backend
* `docs` — product, architecture, decisions, and task notes
* `infra` — Docker, deployment, and local infrastructure files
* `.github/workflows` — CI/CD workflows

## Frontend Standards

* Use TypeScript.
* Use Next.js App Router.
* Prefer server components unless client state or browser APIs are required.
* Use Tailwind CSS for styling.
* Keep components small and readable.
* Use clear loading, empty, error, and success states.
* Do not introduce UI libraries without confirmation.

## Backend Standards

* Use FastAPI.
* Use SQLAlchemy async style.
* Use Alembic for migrations.
* Use Pydantic models for request and response schemas.
* Keep API routes thin.
* Put business logic in service layers.
* Use explicit error handling.
* Add tests for important behavior.

## Database Standards

* Use PostgreSQL as the target database.
* Use UUID primary keys unless there is a clear reason not to.
* Include `created_at` and `updated_at` where appropriate.
* Use indexes intentionally.
* Add audit logs for important user actions.

## Testing Standards

* Backend: pytest.
* Frontend: add tests when behavior is non-trivial.
* Prefer tests for auth, permissions, workflow transitions, and API validation.
* Do not mark a task complete unless relevant tests or checks pass, or the limitation is explained.

## Git Standards

* Use meaningful commit messages.
* Do not mix unrelated changes in one commit.
* Before committing, show a summary of changed files and checks performed.

## Communication Style

* Be direct.
* Explain tradeoffs briefly.
* When uncertain, state assumptions clearly.
* Prefer practical implementation over abstract explanation.
