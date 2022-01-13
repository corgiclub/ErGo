import re

from peewee import MySQLDatabase, Model, DateTimeField, IntegerField, BigAutoField

settings = {
    'host': '###',
    'user': '###',
    'password': '###',
    'port': 3306
}

db = MySQLDatabase("ergo", **settings)


def make_table_name(model_class):
    model_name = model_class.__name__
    return re.sub(
        r'((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1',
        model_name).lower().lstrip("_")


class BaseModel(Model):
    id = BigAutoField(primary_key=True)
    add_time = DateTimeField()
    update_time = DateTimeField()
    delete_time = IntegerField()

    class Meta:
        table_function = make_table_name
        database = db
