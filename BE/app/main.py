import os

#from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import dashboard, scanning, monitoring

#load_dotenv(verbose=True)

app = FastAPI()

origins = ["*"]

app.include_router(dashboard.router)
app.include_router(scanning.router)
app.include_router(monitoring.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}