import json

import pymongo
import os
from bson import json_util

from src.configurations import config


class DBConnection(object):
    def __init__(self, collection_name):
        username = (config.str('INITDB_ROOT_USERNAME') or '')
        pwd = (config.str('INITDB_ROOT_PASSWORD') or '')
        host = (config.str('DB_HOST') or '')
        port = (config.str('DB_PORT') or '')
        db = (config.str('INITDB_DATABASE') or '')

        print("username= " + username)
        print("password= " + pwd)
        print("host= " + host)
        print("port= " + port)
        print("dbname= " + db)

        self.client = pymongo.MongoClient(
            host=host,
            port=int(port),
            username=username,
            password=pwd,
            tz_aware=False,
            document_class=dict
        )
        # print('Mongo URL= ', url)

        self.db_name = config.str('DB_ROOT_NAME')
        self.collection_name = collection_name
        self.collection = self.client[self.db_name][self.collection_name]

    def find_by_page(self, exp, page=0, page_size=20):
        results = list()
        start = page * page_size
        limit = (page + 1) * page_size

        cursor = self.collection.find(exp or {}, {'_id': False})

        for res in cursor.skip(start).limit(limit):
            results.append(json.loads(json_util.dumps(res)))

        return results, start, limit, cursor.count()

    def find(self, exp=None):
        return self.find_by_page(exp)[0]

    def save(self, db_entry):
        self.collection.insert(db_entry)
        return json.loads(json_util.dumps(db_entry))

    def update(self, db_entry, prop):
        self.collection.replace_one({prop: db_entry.get(prop)}, db_entry, True)
        return json.loads(json_util.dumps(db_entry))

    def delete_all(self, db_entry, prop):
        self.collection.delete_many({prop: {'$in': db_entry}})


print('db/__init__ loaded')
