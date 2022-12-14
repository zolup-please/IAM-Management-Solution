import pymongo

class MongoHandler:
    def __init__(self, database, collection, host='localhost', port=27017):
        self._host = host
        self._port = port
        self._database = database
        self._collection = collection
        self._mongo_client = None
        self._mongo_db = None
        self._mongo_collection = None
        self._connect_db()

    def _connect_db(self):
        self._mongo_client = pymongo.MongoClient(self._host, self._port, username='root',  password='root')
        self._mongo_db = self._mongo_client[self._database]
        self._mongo_collection = self._mongo_db[self._collection]

    def count(self):
        return self._mongo_collection.count()
        
    def insert(self, data):
        if isinstance(data, list):
            self._mongo_collection.insert(data)
        elif isinstance(data, dict):
            self._mongo_collection.insert_one(data)

    def find(self, condition):
        return self._mongo_collection.find(condition)

    def _getFindIterator(self):
        return self._mongo_collection.find()

    def __del__(self):
        self._mongo_client.close()

'''
    def delete(self, condition):
        self._mongo_collection.remove(condition)

    def update(self, condition, data):
        self._mongo_collection.update(condition, {"$set": data})

'''