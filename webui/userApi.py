from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Query
from schemas import UserIn, UserOut
from pydantic import AfterValidator

router = APIRouter(
    tags=["user"],
    prefix="/user",
    responses={404: {"description":"Not found"}}
)

def check_validate(data):
    if data == "None":
        raise ValueError("非法参数")
    return data


@router.get("/get")
async def getUser(userName: Annotated[str, Query(min_length=1, description="用户名称",examples=["张三"])]):
    return UserOut(
        userName=userName,
        email="chen@outlook.com",
        sex=1,
        password="",
        create_time=datetime.now()
        )

@router.get("/update")
async def getUser(userName: Annotated[str, AfterValidator(check_validate)]):
    return UserOut(
        userName=userName,
        email="chen@outlook.com",
        sex=1,
        password="",
        create_time=datetime.now()
        )