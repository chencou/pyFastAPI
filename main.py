from fastapi import FastAPI
from webui import web_router 
app = FastAPI()

app.include_router(web_router)

