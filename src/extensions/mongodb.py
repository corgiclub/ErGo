from pymongo import MongoClient
from src.extensions.config import MongoDB


cfg = MongoDB()
client = MongoClient(cfg.host)


def test():
    db = client['test']
    col = db['test_table']
    data = {
        'data': 'test'
    }
    result = col.insert_one(data)
    print(result)


test()
