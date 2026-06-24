from sqlalchemy import DateTime, Uuid

from app.db.base import Base, BaseModel, TimestampMixin, UUIDPrimaryKeyMixin


def test_base_metadata_is_importable_and_has_no_tables() -> None:
    assert Base.metadata is not None
    assert Base.metadata.tables == {}


def test_shared_model_conventions_are_importable() -> None:
    assert issubclass(BaseModel, Base)
    assert BaseModel.__abstract__ is True
    assert UUIDPrimaryKeyMixin is not None
    assert TimestampMixin is not None


def test_shared_model_conventions_define_expected_columns() -> None:
    id_column = UUIDPrimaryKeyMixin.__dict__["id"].column
    created_at_column = TimestampMixin.__dict__["created_at"].column
    updated_at_column = TimestampMixin.__dict__["updated_at"].column

    assert isinstance(id_column.type, Uuid)
    assert id_column.primary_key is True
    assert id_column.default is not None

    assert isinstance(created_at_column.type, DateTime)
    assert created_at_column.type.timezone is True
    assert created_at_column.server_default is not None

    assert isinstance(updated_at_column.type, DateTime)
    assert updated_at_column.type.timezone is True
    assert updated_at_column.server_default is not None
    assert updated_at_column.onupdate is not None
