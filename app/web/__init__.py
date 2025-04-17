from __future__ import annotations

from fastapi import APIRouter

from fastapi.responses import FileResponse

from fastapi.staticfiles import StaticFiles

from .index import router as index_router
from .register import router as register_router

router = APIRouter(
    tags=["web"]
)

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("app/web/static/favicon.ico")

router.include_router(index_router)
router.include_router(register_router)