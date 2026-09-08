from web.App import app

@app.get("/index")
async def fastApi():
    return "hello word!"