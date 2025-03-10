from frozendict import frozendict

from . import config

limits = frozendict({
    "/api/upload": config.UPLOAD_LIMIT,
})