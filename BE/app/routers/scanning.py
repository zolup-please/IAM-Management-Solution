import json
import os.path

from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from .scan import executeScanning, getRecent

import sys
sys.path.append("..")
from modules.mongoHandler import MongoHandler

router = APIRouter(prefix="/scanning")

class ChecklistModel(BaseModel):
    Date: datetime = datetime.now()
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

    database = 'capstone'
    collection = 'recent'
    mongo = MongoHandler(database, collection)
    mongo.insert(report)
    for item in mongo._getFindIterator():
        print(item['Date'])
    del mongo    
    
    return "Scanning finished"

@router.get("/recent")
async def GetRecentReports():
    response = dict()
    count, Reports = getRecent.getRecent()
    response['count'] = count
    response['Reports'] = Reports

    return response