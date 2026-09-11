from commonResult import ErrorCode

SUCCESS: ErrorCode = ErrorCode(0, "成功")

BAD_RQUEST: ErrorCode = ErrorCode(400, "请求参数不正确")
UNAUTHORIZED: ErrorCode = ErrorCode(401, "账号未登录")
FORBIDDEN: ErrorCode = ErrorCode(403, "没有该操作权限")