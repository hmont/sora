from fastapi import APIRouter

from .ban_user import router as ban_user_router
from .delete_upload import router as delete_upload_router

router = APIRouter(
    prefix="",
    tags=["moderation"]
)

router.include_router(ban_user_router)
router.include_router(delete_upload_router)
