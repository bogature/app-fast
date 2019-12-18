from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello22": "World"}
