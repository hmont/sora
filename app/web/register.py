from __future__ import annotations

from fastapi import APIRouter
from fastapi import Request

from app.state.services import templates

router = APIRouter(
    prefix="/register",
    tags=["index"]
)

@router.get("")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})