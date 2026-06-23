from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.db.session import async_session_factory

app = FastAPI(title="OpsPilot API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/db", response_model=None)
async def health_db() -> dict[str, str] | JSONResponse:
    try:
        async with async_session_factory() as db_session:
            await db_session.execute(text("SELECT 1"))
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "error", "database": "unreachable"},
        )

    return {"status": "ok", "database": "reachable"}
