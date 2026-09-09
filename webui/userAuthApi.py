from fastapi import APIRouter
from schemas import UserIn, UserOut, getPasswordHash, verifyPassword
from util import create_access_token
from datetime import date, datetime, timedelta

router = APIRouter(
    tags=["auth"],
    prefix="/auth",
    responses={404: {"description":"Not found"}}
)
    

@router.post("/get")
async def getUser(userIn: UserIn):
    user = UserOut(
        userName=userIn.userName, 
        email=userIn.email, 
        sex=userIn.sex, 
        password=getPasswordHash(userIn.password), 
        create_time=datetime.now()
    )
    return user

@router.post("/sign")
async def signUser(userIn: UserIn):
    userOut = UserOut(
        userName=userIn.userName, 
        email=userIn.email, 
        sex=userIn.sex, 
        password=getPasswordHash(userIn.password), 
        create_time=datetime.now()
    ) 
    return create_access_token({"userName":userOut.userName, "email":userOut.email}, timedelta(60))