from typing import Final

from sqlalchemy import Boolean, CheckConstraint, String, true
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


USER_ROLES: Final[tuple[str, str, str]] = ("admin", "manager", "staff")


class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'manager', 'staff')",
            name="ck_users_role",
        ),
    )

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        index=True,
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=true(),
    )
