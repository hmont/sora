from __future__ import annotations

from fastapi import APIRouter
from fastapi import Request

from app.state.services import templates

router = APIRouter(
    prefix="",
    tags=["index"]
)

@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})