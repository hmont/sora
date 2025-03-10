from fastapi import Request
from fastapi import Response

from limits import parse

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.limits import limits as _limits

from app.state.services import limiter

def _get_ip_address(request: Request) -> str:
    if "X-Forwarded-For" in request.headers:
        return request.headers["X-Forwarded-For"]

    if "X-Real-IP" in request.headers:
        return request.headers["X-Real-IP"]

    if not (request.client and request.client.host):
        return "127.0.0.1"

    return request.client.host

def _get_remote_address(request: Request) -> str:
    if not (request.client and request.client.host):
        return "127.0.0.1"

    return request.client.host

class LimiterMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app
    ):
        super().__init__(app)


    async def dispatch(
        self,
        request: Request,
        call_next
    ) -> Response:
        endpoint = request.url.path

        if not _limits.get(endpoint):
            return await call_next(request)

        _limit = parse(_limits[endpoint])
        _remote_addr = _get_remote_address(request)

        if not limiter.hit(
            _limit,
            _remote_addr,
            endpoint,
            cost=1
        ):
            return Response(
                status_code=429,
                content="Rate limit exceeded"
            )

        return await call_next(request)
