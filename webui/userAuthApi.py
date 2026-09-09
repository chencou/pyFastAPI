from typing import Annotated
from fastapi import APIRouter, Body,Query
from schemas import UserIn, UserOut, getPasswordHash, verifyPassword
from util import create_access_token
from datetime import date, datetime, timedelta

router = APIRouter(
    tags=["auth"],
    prefix="/auth",
    responses={404: {"description":"Not found"}}
)

@router.post("/login")
async def getUser(
    userName: Annotated[str, Query(title="userName", max_length=1, deprecated="用户名称不能为空")],
    password: Annotated[str, Query(title="password", max_length=1, deprecated="密码不能为空")],              
    ):
    email = "email"
    return create_access_token({"userName":userName, "email":email}, timedelta(60))

@router.post("/sign")
async def signUser(userIn: Annotated[UserIn, Body(embed=True)]):
    userOut = UserOut(
        userName=userIn.userName, 
        email=userIn.email, 
        sex=userIn.sex, 
        password=getPasswordHash(userIn.password), 
        create_time=datetime.now()
    ) 
    return create_access_token({"userName":userOut.userName, "email":userOut.email}, timedelta(60))