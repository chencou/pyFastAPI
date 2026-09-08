from main import app

@app.get("/index")
async def fastApi():
    return "hello word!"