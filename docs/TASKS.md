# Tasks

## M1A: Documentation and Configuration Baseline

Status: Complete.

- [x] Add project overview to `README.md`
- [x] Document intended tech stack
- [x] Document monorepo structure
- [x] Mark local development commands as planned, not available
- [x] Add staged roadmap to `docs/ROADMAP.md`
- [x] Record initial architecture decisions in `docs/DECISIONS.md`
- [x] Add non-secret environment placeholders to `.env.example`
- [x] Review M1A changes
- [x] Approve moving to M1B

## M1B: FastAPI Health Check and Backend Test Setup

Status: Complete.

- [x] Create minimal backend project metadata in `apps/api/pyproject.toml`
- [x] Expose a FastAPI `app` from `apps/api/app/main.py`
- [x] Add `GET /health` returning `{"status": "ok"}`
- [x] Add one pytest test for `/health`
- [x] Update `README.md` with available backend run and test commands
- [ ] Approve moving to M1C
