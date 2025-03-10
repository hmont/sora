from __future__ import annotations

from sqlalchemy import select

from fastapi import APIRouter
from fastapi import File
from fastapi import Request
from fastapi import UploadFile
from fastapi import Response

from app.models import users

router = APIRouter(
    prefix="/ban",
    tags=["ban-user"]
)

@router.post(
    path="",
    tags=["ban"]
)
async def ban_user(
    request: Request,
    response: Response,
    user_id: int | None = None,
    username: str | None = None,
):
    if not user_id and not username:
        return Response(
            status_code=418, # TODO: change status code
            content="You must provide either user_id or username"
        )

    return Response(
        status_code=200, # TODO: change status code
        content="User has been banned"
    )
