import json
import os.path

from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from .scan import executeScanning

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
    report = executeScanning.executeScanning(checked.dict())
    return report

@router.get("/recent")
async def GetRecentReports():
    pass