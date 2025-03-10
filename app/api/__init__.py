from __future__ import annotations

from fastapi import APIRouter

from .upload import router as upload_router
from .register import router as register_router

from .moderation import router as moderation_router

api_router = APIRouter(
    prefix="/api",
    tags=["api"]
)

api_router.include_router(upload_router)
api_router.include_router(register_router)
api_router.include_router(moderation_router)