
import pymongo
from mongodb import get_collection


col = get_collection('group_chat', '722077615')

for line in col.find():
    try:
        col.update_one(line,
                       {
                           '$set':
                               {
                                   'uid': str(line['uid'])
                               }
                       })
    except:
        continue

# result = col.update_many({}, {'$set': {'counts': 1}})

