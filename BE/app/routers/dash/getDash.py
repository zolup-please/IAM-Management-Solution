from .tmp import test

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
    template['IAMActivities'] = getGraph()

    # Changes
    template['Changes'] = getChanges()

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


def getGraph():
    ret = {
	"id": "로그 발생",
	"color": "hsl(164, 70%, 50%)",
	'data': [{
		'x': '04:30:00',
		'y': 14
	}, {
		'x': '05:00:00',
		'y': 6
	}, {
		'x': '05:30:00',
		'y': 25
	}, {
		'x': '06:00:00',
		'y': 15
	}, {
		'x': '06:30:00',
		'y': 20
	}, {
		'x': '07:00:00',
		'y': 6
	}, {
		'x': '07:30:00',
		'y': 24
	}, {
		'x': '08:00:00',
		'y': 6
	}, {
		'x': '08:30:00',
		'y': 27
	}, {
		'x': '09:00:00',
		'y': 84
	}, {
		'x': '09:30:00',
		'y': 63
	}, {
		'x': '10:00:00',
		'y': 19
	}, {
		'x': '10:30:00',
		'y': 23
	}, {
		'x': '11:00:00',
		'y': 17
	}, {
		'x': '11:30:00',
		'y': 82
	}, {
		'x': '12:00:00',
		'y': 93
	}, {
		'x': '12:30:00',
		'y': 74
	}, {
		'x': '13:00:00',
		'y': 86
	}, {
		'x': '13:30:00',
		'y': 51
	}, {
		'x': '14:00:00',
		'y': 54
	}, {
		'x': '14:30:00',
		'y': 52
	}, {
		'x': '15:00:00',
		'y': 44
	}, {
		'x': '15:30:00',
		'y': 38
	}, {
		'x': '16:00:00',
		'y': 27
	}]
}
    return ret
    pass

def getChanges():
    database = 'capstone'
    collection = 'Users'
    mongo = MongoHandler(database, collection)

    for item in mongo.get_recent_N_Iterator(1):
        del item['_id']

    tt = test(item)

    del mongo

    return tt.result


if __name__=='__main__':
    getChanges()