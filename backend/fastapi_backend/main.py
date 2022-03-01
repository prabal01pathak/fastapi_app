from fastapi import FastAPI

app = FastAPI()

@app.get("/fast")
async def hello():
    return {
        "message": "Hello World"
    }
