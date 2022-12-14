

import sys
sys.path.append("../../")
from modules.mongoHandler import MongoHandler

def getRecent():
    database = 'capstone'
    collection = 'recent'
    mongo = MongoHandler(database, collection)

    Report = []

    MAX = 30
    count = mongo.estimated_document_count()
    if(MAX < count):
        count = MAX
    
    d = dict()
    for item in mongo.get_recent_N_Iterator(count):
        del item['_id']
        Report.append(item)
    
    del mongo

    return count, Report