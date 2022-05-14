from src.extensions.mongodb import get_collection

col = get_collection('group_chat', '1051061379')

c = col.find({'uid': '1300401733', 'type': 'text'})
d = col.find({'type': 'text'})
print(c.count() / d.count())
print(col.find_one())
