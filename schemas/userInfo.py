from typing import Literal
from pydantic import BaseModel, EmailStr, Field
from pwdlib import PasswordHash
from datetime import date, datetime



password_hash = PasswordHash.recommended()
class UserIn(BaseModel):
    userName: str = Field(
        alias="userName",
        title="用户名称",
        description="输入用户名称最大32，最小1个字符",
        max_length=32,
        min_length=1,
        examples=["用户名称"],
    )
    email: EmailStr = Field(
        alias="email",
        title="邮箱",
        examples=["saned@163.com"]
    )
    sex: Literal[0, 1] = Field(
        alias="sex",
        title="性别 0：女，1:男",
        examples=[0],
        default=0
    )
    password: str = Field(
        alias="password",
        title="密码",
        description="密码不能为空",
        max_length=128,
        min_length=1,
        examples=["qW123456@"],
    )
    


class UserOut(BaseModel):
    userName: str
    email: EmailStr
    sex: int
    password: str
    create_time: datetime


def get_password_hash(password:str):
    return password_hash.hash(password)


def verify_password(verify_password:str, hash_password):
    return password_hash.verify(verify_password, hash_password)
