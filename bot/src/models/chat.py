from peewee import BigIntegerField, CharField, IntegerField

from src.models import db, BaseModel


class Chat(BaseModel):
    group_id = BigIntegerField()
    user_id = BigIntegerField()
    message_id = IntegerField()
    type = CharField(max_length=10)


class ChatText(BaseModel):
    chat_id = BigIntegerField(default=0, help_text='chat id')
    text = CharField(max_length=1023, default='', help_text='纯文本内容')


if __name__ == '__main__':
    print(Chat.get_by_id(2))
