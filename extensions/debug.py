import pymongo
from extensions.load_config import load_config


config = load_config('log_to_database')
client = pymongo.MongoClient(config.db_host)
col = client['Images']['ImagesInGroupMessage']
col.create_index('mentioned_times')
