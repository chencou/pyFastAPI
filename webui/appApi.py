from fastapi import APIRouter

router = APIRouter()

@router.get("/index")
async def fastApi():
    return "hello word!"

