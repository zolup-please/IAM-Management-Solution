from fastapi import APIRouter

from .dash.getDash import getDash

router = APIRouter(prefix="/dashboard")

@router.get("/")
async def dashboard():
    return getDash()