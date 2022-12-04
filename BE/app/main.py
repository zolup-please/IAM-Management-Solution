from fastapi import FastAPI

from routers import dashboard, scanning, monitoring


app = FastAPI()

app.include_router(dashboard.router)
app.include_router(scanning.router)
app.include_router(monitoring.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}