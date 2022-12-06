import json
import os.path

from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from scan import distributor

router = APIRouter(prefix="/scanning")

class ChecklistModel(BaseModel):
    scannedDatetime: datetime = datetime.now()
    checkedCount: int
    checkedList: list = []
    

@router.get("/")
async def ScanningList():
    filepath = os.path.dirname(__file__) + '/../data/ScanningList.json'
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

@router.post("/")
async def StartScanning(checked: ChecklistModel):

    return checked

@router.get("/recent")
async def GetRecentReports():
    pass