from __future__ import annotations

import uvicorn

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from app.state import services

from app.api import api_router
from app.web import router as web_router

from app.core import config

from app.middleware.limiter import LimiterMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await services.database.connect()

        app.state.limiter = services.limiter

        yield
    finally:
        await services.database.disconnect()

app = FastAPI(
    lifespan=lifespan,
    redoc_url=None,
    docs_url=None
)

app.include_router(api_router)
app.include_router(web_router)

app.add_middleware(LimiterMiddleware)

app.mount("/static", StaticFiles(directory="app/web/static"), name="static")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.SORA_HOST,
        port=config.SORA_PORT,
        workers=config.WORKERS
    )