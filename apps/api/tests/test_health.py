from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from app import main as app_main


client = TestClient(app_main.app)


class FakeSession:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error

    async def execute(self, statement: object) -> None:
        if self.error is not None:
            raise self.error


class FakeSessionContext:
    def __init__(
        self,
        session: FakeSession | None = None,
        error: Exception | None = None,
    ) -> None:
        self.session = session or FakeSession()
        self.error = error

    async def __aenter__(self) -> FakeSession:
        if self.error is not None:
            raise self.error
        return self.session

    async def __aexit__(
        self,
        exc_type: object,
        exc: object,
        traceback: object,
    ) -> None:
        return None


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_db_returns_reachable_when_query_succeeds(monkeypatch) -> None:
    monkeypatch.setattr(
        app_main,
        "async_session_factory",
        lambda: FakeSessionContext(),
    )

    response = client.get("/health/db")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "reachable"}


def test_health_db_returns_503_when_query_fails(monkeypatch) -> None:
    monkeypatch.setattr(
        app_main,
        "async_session_factory",
        lambda: FakeSessionContext(FakeSession(SQLAlchemyError("connection failed"))),
    )

    response = client.get("/health/db")

    assert response.status_code == 503
    assert response.json() == {"status": "error", "database": "unreachable"}


def test_health_db_returns_503_when_session_open_fails(monkeypatch) -> None:
    monkeypatch.setattr(
        app_main,
        "async_session_factory",
        lambda: FakeSessionContext(error=ConnectionRefusedError("connection refused")),
    )

    response = client.get("/health/db")

    assert response.status_code == 503
    assert response.json() == {"status": "error", "database": "unreachable"}
