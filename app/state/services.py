from __future__ import annotations

from redis.asyncio import Redis

from fastapi.templating import Jinja2Templates

from limits import storage
from limits import strategies

from app.core import config

from app.adapters.database import Database

database = Database(config.MYSQL_DSN)

templates = Jinja2Templates(directory="app/web/templates")

# redis = Redis.from_url(config.REDIS_URI)

redis_storage = storage.RedisStorage(config.REDIS_URI)

limiter = strategies.FixedWindowRateLimiter(redis_storage)