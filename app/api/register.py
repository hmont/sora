from typing import Any

from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import Depends

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/register",
    tags=["register"]
)

@router.post(
    path="",
    tags=["api_register"]
)
async def register(
    request: Request,
    response: Response,
    data: OAuth2PasswordRequestForm = Depends()
):
    pass
