import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
col = db["test_collection"]

dit = {"name": "name", "alexa": "10000", "url": "pppp"}

x = col.insert_one(dit)
print(x)
