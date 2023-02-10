from fastapi import FastAPI

import random
from datetime import datetime


app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "It is alive!"}


@app.get("/thud", tags=["thud"])
async def get_thud() -> dict:
    number = random.randrange(1, 10**10)

    return {"id": number, "created_at":  datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
