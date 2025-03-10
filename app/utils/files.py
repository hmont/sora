import secrets
import string
import os

from fastapi import UploadFile

from typing import Optional

from app.core import config

from . import VALID_CHARS

def generate_upload_id(
    file: UploadFile,
    length: Optional[int] = None
) -> str:
    if not length:
        length = config.UPLOAD_ID_LENGTH

    return "".join(secrets.choice(VALID_CHARS) for _ in range(length))
