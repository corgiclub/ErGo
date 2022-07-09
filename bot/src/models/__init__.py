import re

from peewee import MySQLDatabase, Model, DateTimeField, IntegerField, BigAutoField, OperationalError
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


from src.models.settings import settings


# settings = {
#     'host': '',
#     'user': '',
#     'password': '',
#     'port': 10003
# }

# db = MySQLDatabase("ergo", **settings)


class RetryMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    _instance = None

    @staticmethod
    def get_db_instance():
        if not RetryMySQLDatabase._instance:
            RetryMySQLDatabase._instance = RetryMySQLDatabase(
                "ergo",
                max_connections=24,
                stale_timeout=300,
                **settings
            )
        return RetryMySQLDatabase._instance


db = RetryMySQLDatabase.get_db_instance()
db.execute_sql("SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;")


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

