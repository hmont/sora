from __future__ import annotations

import aiofiles
import os

from datetime import datetime

from fastapi import APIRouter
from fastapi import File
from fastapi import Request
from fastapi import UploadFile
from fastapi import Response

from app.models import uploads

from app.core import config

from app.utils import files

router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)

@router.post(
    path="",
    tags=["upload"]
)
async def upload(
    request: Request,
    response: Response,
    file: UploadFile
):
    if not file.filename:
        return Response(
            status_code=418, # TODO: change status code
            content="No filename provided"
        )

    upload = await uploads.create_from_file(file)

    return "done"