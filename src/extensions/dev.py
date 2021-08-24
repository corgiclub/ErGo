# from src.extensions.imghdr_byte import what
#
# with open('original.png', 'rb') as fi:
#     by = fi.read()
#     print(type(what(by)))
#     print(what(by))
#
import pymongo
from mongodb import get_collection


col = get_collection('picture', 'chat')

print(col.create_index([("file", pymongo.HASHED)]))

