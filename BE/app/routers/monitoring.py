import json
import os.path

from fastapi import APIRouter

router = APIRouter(prefix="/monitoring")

@router.get("/")
async def MonitoringList():
    filepath = os.path.dirname(__file__) + '/../data/MonitoringList.json'
    with open(filepath, "r") as f:
        data = json.load(f)
    return data