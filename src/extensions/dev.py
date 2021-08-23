# from src.extensions.imghdr_byte import what
#
# with open('original.png', 'rb') as fi:
#     by = fi.read()
#     print(type(what(by)))
#     print(what(by))
#

from mongodb import get_collection


col = get_collection('group_chat', '710719704')

print(col.find_one({"text": "dsds扇"}))

