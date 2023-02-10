import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("thud_generator.main:app", host="0.0.0.0", port=8000, reload=True)
