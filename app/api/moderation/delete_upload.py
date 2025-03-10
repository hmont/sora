from __future__ import annotations

from sqlalchemy import select
from sqlalchemy import delete

from fastapi import APIRouter
from fastapi import File
from fastapi import Request
from fastapi import UploadFile
from fastapi import Response

from app.models import uploads

from app.state.services import database

router = APIRouter(
    prefix="/delete_upload",
    tags=["upload"]
)

@router.post(
    path="",
    tags=["delete-upload"]
)
async def delete_upload(
    request: Request,
    response: Response,
    id: int | None = None,
    upload_id: str | None = None
):
    if not id and not upload_id:
        return Response(
            status_code=418, # TODO: change status code
            content="You must provide either id or upload_id"
        )

    upload = await uploads.fetch_one(
        id=id,
        upload_id=upload_id
    )

    if not upload:
        return Response(
            status_code=404,
            content="No such upload exists"
        )

    query = delete(uploads.UploadsTable).where(uploads.UploadsTable.id == upload["id"])

    await database.execute(query)

    return Response(
        status_code=200,
        content="Upload deleted"
    )
