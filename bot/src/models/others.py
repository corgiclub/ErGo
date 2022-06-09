from peewee import BigIntegerField, CharField, SmallIntegerField, BooleanField

from src.models import BaseModel


class Note(BaseModel):
    note = CharField(max_length=32, default='')
    value = CharField(max_length=255, default='')
    group_id = BigIntegerField(default=0)
