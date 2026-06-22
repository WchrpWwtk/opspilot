# ~/.codex/AGENTS.md

## Global Working Preferences

* Prefer concise explanations.
* Work in small steps.
* Always inspect the existing code before changing it.
* Never assume project structure; verify it first.
* Before implementation, provide a short plan.
* After implementation, summarize:

  * files changed
  * what changed
  * checks run
  * remaining risks
* Ask before adding new production dependencies.
* Do not expose or modify secrets.
* Do not run destructive commands such as deleting files, dropping databases, or force-pushing without explicit confirmation.

## Preferred Stack

* Package manager: pnpm for JavaScript/TypeScript projects.
* Frontend: Next.js, TypeScript, Tailwind CSS.
* Backend: FastAPI, SQLAlchemy async, Alembic, PostgreSQL.
* Testing: pytest for Python, Vitest/Playwright when needed for frontend.
* Local development: Docker Compose where useful.

## Review Discipline

* Keep diffs small.
* Prefer simple, maintainable code over clever abstractions.
* Add comments only when they explain non-obvious decisions.
* Do not over-engineer early MVP features.
