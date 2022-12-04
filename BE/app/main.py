import os

from dotenv import load_dotenv
from fastapi import FastAPI

from routers import dashboard, scanning, monitoring

load_dotenv(verbose=True)

app = FastAPI()

app.include_router(dashboard.router)
app.include_router(scanning.router)
app.include_router(monitoring.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}