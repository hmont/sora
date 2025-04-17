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
    username = data.username
    password = data.password

    resp = {}

    query = select(users.UsersTable).where(users.UsersTable.username == username)

    if await database.fetch_one(query) is not None:
        resp["success"] = False
        resp["message"] = "User already exists."

        return JSONResponse(resp)

    resp["success"] = True
    resp["message"] = None
    return JSONResponse(resp)
