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
    return col.insert_one(data)
    # print(result)


def get_collection(db_name: str, col_name: str):
    return client[db_name][col_name]


# test()
