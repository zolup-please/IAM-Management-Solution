import json
import os.path

from fastapi import APIRouter

router = APIRouter(prefix="/scanning")

@router.get("/")
async def ScanningList():
    filepath = os.path.dirname(__file__) + '/../data/ScanningList.json'
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

@router.post("/")
async def StartScanning():
    pass

@router.get("/recent")
async def GetRecentReports():
    pass