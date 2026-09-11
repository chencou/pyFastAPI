from pydantic import BaseModel
from typing import Any

class ErrorCode(BaseModel):
    code:int = 0
    msg:str = None


class CommonResult(BaseModel):
    code:int = 0
    data: Any | None = None
    msg:str | None = None
    requestId:str =None

    
    @classmethod
    def success(self, data:Any) -> "CommonResult":
        self.data = data
        self.code = 0
        return self

    @classmethod
    def error(self, code:int, msg:str) -> "CommonResult":
        self.code = code
        self.msg = msg
        return self

    @classmethod
    def error(self, errorMsg: ErrorCode) -> "CommonResult":
        self.code = errorMsg.code
        self.msg = errorMsg.msg
        return self


    @classmethod
    def isSuccess(self) -> bool:
        return self.code == 0





    