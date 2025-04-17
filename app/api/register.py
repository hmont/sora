from typing import Any

from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import Depends

from fastapi.responses import JSONResponse

from sqlalchemy import select

from ..models import users

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app.state.services import database

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
    print(data)