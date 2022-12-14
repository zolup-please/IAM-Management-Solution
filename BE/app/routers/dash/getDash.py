
import sys
sys.path.append("../../")
from modules.mongoHandler import MongoHandler

def getDash():
    template = {
        "RecentReport": {
            "Counts": 0,
            "Reports": []
        },
        "IAMActivities": {},
        "Changes": {
            "Total": 0,
            "Created": 0,
            "Deleted": 0
        }
    }

    # RecentReport
    count, reports = loadReport()
    template['RecentReport']['Counts'] = count
    template['RecentReport']['Reports'] = reports

    # IAMActivities

    # Changes

    return template


def loadReport():
    database = 'capstone'
    collection = 'recent'
    mongo = MongoHandler(database, collection)

    Report = []

    MAX = 10
    count = mongo.estimated_document_count()
    if(MAX < count):
        count = MAX
    
    d = dict()
    for item in mongo.get_recent_N_Iterator(count):
        d['Date'] = item['Date']
        d['Checked'] = item['Checked']
        d['Detected'] = item['Detected']
        Report.append(d)
    
    return count, Report


if __name__=='__main__':
    b = getDash()

    print(b)