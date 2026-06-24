from sqlalchemy import Boolean, DateTime, String, Uuid, UniqueConstraint

from app.db.base import Base


def test_user_model_can_be_imported() -> None:
    from app.models.user import USER_ROLES, User

    assert User.__tablename__ == "users"
    assert USER_ROLES == ("admin", "manager", "staff")


def test_user_table_is_registered_in_base_metadata() -> None:
    from app.models.user import User

    assert "users" in Base.metadata.tables
    assert Base.metadata.tables["users"] is User.__table__


def test_user_table_has_expected_columns() -> None:
    from app.models.user import User

    columns = User.__table__.columns

    assert set(columns.keys()) == {
        "id",
        "email",
        "full_name",
        "role",
        "is_active",
        "created_at",
        "updated_at",
    }

    assert isinstance(columns["id"].type, Uuid)
    assert columns["id"].primary_key is True
    assert columns["id"].nullable is False

    assert isinstance(columns["email"].type, String)
    assert columns["email"].type.length == 320
    assert columns["email"].nullable is False

    assert isinstance(columns["full_name"].type, String)
    assert columns["full_name"].nullable is False

    assert isinstance(columns["role"].type, String)
    assert columns["role"].nullable is False

    assert isinstance(columns["is_active"].type, Boolean)
    assert columns["is_active"].nullable is False
    assert columns["is_active"].default is not None
    assert columns["is_active"].server_default is not None

    assert isinstance(columns["created_at"].type, DateTime)
    assert columns["created_at"].type.timezone is True
    assert columns["created_at"].nullable is False

    assert isinstance(columns["updated_at"].type, DateTime)
    assert columns["updated_at"].type.timezone is True
    assert columns["updated_at"].nullable is False


def test_user_email_has_unique_index_or_constraint() -> None:
    from app.models.user import User

    table = User.__table__
    unique_email_constraints = [
        constraint
        for constraint in table.constraints
        if isinstance(constraint, UniqueConstraint)
        and list(constraint.columns.keys()) == ["email"]
    ]
    email_indexes = [
        index for index in table.indexes if list(index.columns.keys()) == ["email"]
    ]

    assert unique_email_constraints or any(index.unique for index in email_indexes)
    assert email_indexes
