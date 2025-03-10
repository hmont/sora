from __future__ import annotations

from datetime import datetime

from typing import TypedDict
from typing import cast

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import insert

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

from app.state import services

class UsersTable(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, nullable=False, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), nullable=False)
    password_hashed: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    created: Mapped[datetime] = mapped_column(nullable=False)
    priv: Mapped[int] = mapped_column(Integer, nullable=False, server_default="1")
    upload_key: Mapped[str] = mapped_column(String(32), nullable=False)


class User(TypedDict):
    id: int
    username: str
    password_hashed: str
    email: str
    created: datetime
    priv: int
    upload_key: str


async def fetch_one(
    id: int | None = None,
    username: str | None = None,
    email: str | None = None,
    upload_key: str | None = None
) -> User | None:
    if not any((id, username, email, upload_key)):
        raise ValueError("One of id, username, email, or upload_key must be provided.")

    query = select(UsersTable)

    if id:
        query = query.where(UsersTable.id == id)

    if username:
        query = query.where(UsersTable.username == username)

    if email:
        query = query.where(UsersTable.email == email)

    if upload_key:
        query = query.where(UsersTable.upload_key == upload_key)

    query = str(query)

    user = await services.database.fetch_one(query)

    return cast(User, user) if user else None


async def fetch_many(priv: int | None) -> list[User]:
    if not priv:
        raise ValueError("priv must be provided.")

    query = select(UsersTable).where(UsersTable.priv == priv)

    query = str(query)

    users = await services.database.fetch_all(query)

    return cast(list[User], users)