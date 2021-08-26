
import pymongo
from mongodb import get_collection


col = get_collection('picture', 'chat')

result = col.update_many({}, {'$set': {'counts': 1}})

