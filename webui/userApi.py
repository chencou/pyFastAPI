from util import logging
from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Query, Header, Cookie
from schemas import UserIn, UserOut
from pydantic import AfterValidator, BaseModel, Field
from schemas import CommonResult


router = APIRouter(
    tags=["user"],
    prefix="/user",
    responses={404: {"description":"Not found"}}
)

def check_validate(data):
    if data == "None":
        raise ValueError("非法参数")
    return data


class authHeader(BaseModel):
    app_id:str = Field(min_length=1, description="应用编号",examples=["test"])
    app_public_key:str | None


class authCookies(BaseModel):
    lang: str = "ch"
    userId: int
    

@router.get("/get")
async def getUser(
    headers: Annotated[authHeader, Header()],
    userName: Annotated[str, Query(min_length=1, description="用户名称",examples=["张三"])]) -> CommonResult:
    logging.info(f"headers=({headers})")
    return CommonResult.success(UserOut(
        userName=userName,
        email="chen@outlook.com",
        sex=1,
        password="",
        create_time=datetime.now()
        ))

@router.get("/update")
async def getUser(
    cookies: Annotated[authCookies, Cookie()],
    userName: Annotated[str, AfterValidator(check_validate)]) -> CommonResult:
    logging.info(f"cookies=({cookies})")
    return CommonResult.success(UserOut(
        userName=userName,
        email="chen@outlook.com",
        sex=1,
        password="",
        create_time=datetime.now()
        ))