import json

import pymongo
from bson import json_util

import src.configurations as config


class Database(object):
    def __init__(self, collection_name):
        self.client = pymongo.MongoClient(config.MONGO_DB_CONNECTION_URL)
        self.db_name = config.DB_ROOT_NAME
        self.collection_name = collection_name
        self.collection = self.client[ self.db_name ][ self.collection_name ]

    def set_collection(self):
        pass

    def find(self, exp=None):
        results = list()
        for res in self.collection.find(exp or { }):
            results.append(json.loads(json_util.dumps(res)))
        return results

    def save(self, db_entry):
        self.collection.insert(db_entry)
        return json.loads(json_util.dumps(db_entry))

    def update(self, db_entry, prop):
        self.collection.replace_one({ prop: db_entry.get(prop) }, db_entry, False)
        return json.loads(json_util.dumps(db_entry))

    def delete_all(self, db_entry, prop):
        self.collection.delete_many({ prop: { '$in': db_entry } })

    print('db/__init__ loaded')
