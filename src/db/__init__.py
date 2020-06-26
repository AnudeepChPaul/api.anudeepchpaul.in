# from rethinkdb import RethinkDB
import src.configurations as config
import pymongo
from bson import json_util, ObjectId
import json


class Database(object):
    def __init__(self, collection_name):
        self.client = pymongo.MongoClient(config.MONGO_DB_CONNECTION_URL)
        self.db_name = config.DB_ROOT_NAME
        self.collection_name = collection_name
        self.collection = self.client[self.db_name][self.collection_name]

    def set_collection(self):
        pass

    def find(self):
        results = list()
        for res in self.collection.find():
            # results.append(res)
            results.append(json.loads(json_util.dumps(res)))
        return results


print('db/__init__ loaded')
