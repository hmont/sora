from __future__ import annotations

import os

from datetime import datetime

from typing import TypedDict
from typing import cast

from fastapi import UploadFile

from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy import insert

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

from app.state import services

from app.utils import files

class UploadsTable(Base):
    __tablename__ = "uploads"

    id: Mapped[int] = mapped_column(autoincrement=True, nullable=False, primary_key=True)
    filename: Mapped[str] = mapped_column(String(32), nullable=False)
    upload_id: Mapped[str] = mapped_column(String(32), nullable=False)
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)

    uploader_id: Mapped[int] = mapped_column(nullable=False)
    uploader_name: Mapped[str] = mapped_column(String(32), nullable=False)
    uploaded: Mapped[datetime] = mapped_column(nullable=False)


class Upload(TypedDict):
    id: int
    filename: str
    upload_id: str
    original_filename: str
    uploader_id: int
    uploader_name: str
    uploaded: datetime


async def fetch_one(
    id: int | None = None,
    upload_id: str | None = None
) -> Upload | None:
    """Fetch a single upload from the database with the given ID or upload_id.

    Args:
        id (int | None, optional): The integer ID of the upload. Defaults to None.
        upload_id (str | None, optional): The string upload_id of the upload. Defaults to None.

    Raises:
        ValueError: if neither id nor upload_id are provided.

    Returns:
        Upload | None: The upload with the given ID or upload_id, or None if no such upload exists.
    """
    if not id and not upload_id:
        raise ValueError("Either id or upload_id must be provided")

    query = select(UploadsTable)

    if id:
        query = query.where(UploadsTable.id == id)

    if upload_id:
        query = query.where(UploadsTable.upload_id == upload_id)

    query = str(query)

    upload = await services.database.fetch_one(query)

    return cast(Upload, upload) if upload else None


async def fetch_many(
    uploader_id: int | None = None,
    uploader_name: str | None = None,
    page: int | None = None,
    page_size: int | None = None
) -> list[Upload]:
    """Fetch all uploads from the database with the given uploader integer ID or username.

    Args:
        uploader_id (int | None, optional): The integer ID of the uploader. Defaults to None.
        uploader_name (str | None, optional): The name of the uploader. Defaults to None.
        page (int | None, optional): The page of uploads to fetch. Defaults to None.
        page_size (int | None, optional): How many uploads to fetch per page. Defaults to None.

    Returns:
        list[Upload]: A list of uploads with the given uploader ID or username.
    """

    if not uploader_id and not uploader_name:
        raise ValueError("Either an uploader ID or uploader name must be provided")

    query = select(UploadsTable)

    if uploader_id:
        query = query.where(UploadsTable.uploader_id == uploader_id)

    if uploader_name:
        query = query.where(UploadsTable.uploader_name == uploader_name)

    if page and page_size:
        query = query.limit(page_size).offset(page_size * (page - 1))

    uploads = await services.database.fetch_all(query)

    return cast(list[Upload], uploads)


async def create(
    filename: str,
    upload_id: str,
    original_filename: str,
    uploader_id: int,
    uploader_name: str,
    uploaded: datetime
) -> Upload:
    """Create a new upload in the database.

    Args:
        filename (str): The filename of the upload.
        upload_id (str): The upload_id of the upload.
        original_filename (str): The original filename of the upload.
        uploader_id (int): The integer ID of the uploader.
        uploader_name (str): The name of the uploader.
        uploaded (int): The timestamp of the upload.

    Returns:
        Upload: The newly created upload.
    """

    insert_query = insert(UploadsTable).values(
        filename=filename,
        upload_id=upload_id,
        original_filename=original_filename,
        uploader_id=uploader_id,
        uploader_name=uploader_name,
        uploaded=uploaded
    )

    rec_id = await services.database.execute(insert_query)

    fetch_query = select(UploadsTable).where(UploadsTable.id == rec_id)

    upload = await services.database.fetch_one(fetch_query)

    assert upload is not None

    return cast(Upload, upload)

async def create_from_file(file: UploadFile) -> Upload:
    assert file.filename

    _file_ext = os.path.splitext(file.filename)[-1]
    _upload_id = files.generate_upload_id(file)

    return await create(
        original_filename = file.filename,
        filename = _upload_id + _file_ext,
        upload_id=_upload_id,
        uploader_id = 1,
        uploader_name = "test",
        uploaded = datetime.now()
    )