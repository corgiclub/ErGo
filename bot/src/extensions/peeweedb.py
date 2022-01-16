from peewee import *

database = MySQLDatabase()


class MessageSegment(Model):
    message_id = BigIntegerField(default=0)
    sender_id = BigIntegerField(default=0)
    group_id = BigIntegerField(default=0)



