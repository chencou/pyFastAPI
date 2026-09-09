from fastapi import FastAPI
from webui import web_router, user_auth_router, user_router 
app = FastAPI()

app.include_router(web_router)
app.include_router(user_auth_router)
app.include_router(user_router)

