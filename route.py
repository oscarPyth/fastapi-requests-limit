from fastapi import APIRouter, Request

from fastapi_requests_limit.limiter_rest import LimiterDecorator as limiter_decorator

router = APIRouter()


@router.get("/")
@limiter_decorator(time=5, count_target=3)
async def read_users(request: Request):
    return [{"username": "Rick"}, {"username": "Morty"}]
