import uvicorn
from fastapi import FastAPI

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("thud_generator.api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()