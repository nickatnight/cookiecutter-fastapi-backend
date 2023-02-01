from fastapi import APIRouter


# from fastapi_limiter.depends import RateLimiter


router = APIRouter()


@router.get("/ping", tags=["health"])
async def pong():
    # some async operation could happen here
    # example: `data = await get_all_datas()`
    return {"ping": "pong!"}
