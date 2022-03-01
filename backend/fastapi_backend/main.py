from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
async def hello():
    return {
        "message": "Hello World"
    }
