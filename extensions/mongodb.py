import pymongo
from load_config import load_config

config = load_config('log_to_database')
client = pymongo.MongoClient(config.db_host)


def log_info(group, member):
    db = client['InteractionObjects']
    groups_col = db['groups']
    users_col = db['users']

    if group_dict := groups_col.find_one({"group_id": group.id}):
        if group_dict['group_names'][-1] != group.name:
            group_names = group_dict['group_names'] + [group.name]
            groups_col.update_one({"group_id": group.id}, {'$set': {'group_names': group_names}})
    else:
        group_dict = {
            'group_id': group.id,
            'group_names': [group.name]
        }
        groups_col.insert_one(group_dict)

    if user_dict := users_col.find_one({"user_id": member.id}):
        if member.name not in user_dict['user_names']:
            user_names = user_dict['user_names'] + [member.name]
            users_col.update_one({"user_id": member.id}, {'$set': {'user_names': user_names}})
        if member.group.id not in user_dict['user_groups']:
            user_groups = user_dict['user_groups'] + [member.group.id]
            users_col.update_one({"user_id": member.id}, {'$set': {'user_groups': user_groups}})
    else:
        user_dict = {
            'user_id': member.id,
            'user_names': [member.name],
            'user_groups': [member.group.id]
        }
        users_col.insert_one(user_dict)


def log_message(message, group, member):
    db = client['GroupChats']
    group = db[str(group.id)]



def log_text():
    pass


def log_picture():
    pass


def log_audio():
    pass


def log_debug():
    db = client['InteractionObjects']
    groups_col = db['groups']
    users_col = db['users']

    print([x for x in groups_col.find()])
    print([x for x in users_col.find()])
