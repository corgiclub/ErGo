import pymongo
from _old.extensions import load_config


config = load_config('log_to_database')
client = pymongo.MongoClient(config.db_host)
col = client['Images']['ImagesInGroupMessage']
col.create_index('mentioned_times')
