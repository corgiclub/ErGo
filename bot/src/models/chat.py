from peewee import BigIntegerField, CharField, IntegerField, SmallIntegerField, FloatField

from src.models import db, BaseModel


class Chat(BaseModel):
    group_id = BigIntegerField()
    user_id = BigIntegerField()
    message_id = IntegerField()
    type = SmallIntegerField()


class ChatBaseModel(BaseModel):
    chat_id = BigIntegerField(default=0, help_text='chat id')


class ChatText(ChatBaseModel):
    text = CharField(max_length=1023, default='', help_text='纯文本内容')


class ChatFace(ChatBaseModel):
    face_id = BigIntegerField(default=0)


class ChatImage(ChatBaseModel):
    image_id = BigIntegerField(default=0)
    qq_hash = CharField(max_length=32, default='', help_text='QQ 返回的hash值')
    url = CharField(max_length=1023, default='', help_text='图片链接')


class ChatRecord(ChatBaseModel):
    file_url = CharField(max_length=1023, default='')
    file_name = CharField(max_length=1023, default='')


class ChatVideo(ChatBaseModel):
    file_url = CharField(max_length=1023, default='')
    file_name = CharField(max_length=1023, default='')


class ChatAt(ChatBaseModel):
    qq = BigIntegerField(default=0, help_text='at的qq号, 1表示全体成员')


class ChatPoke(ChatBaseModel):
    type = SmallIntegerField(default=0)
    qq = BigIntegerField(default=0)
    name = CharField(max_length=10, default='')


class ChatShare(ChatBaseModel):
    url = CharField(max_length=1023, default='')
    title = CharField(max_length=255, default='')


class ChatContact(ChatBaseModel):
    type = SmallIntegerField(default=0)
    contact_id = BigIntegerField(default=0)


class ChatLocation(ChatBaseModel):
    lat = FloatField(default=0)
    lot = FloatField(default=0)


class ChatReply(ChatBaseModel):
    message_id = BigIntegerField(default=0)


class ChatForward(ChatBaseModel):
    message_id = BigIntegerField(default=0)


class ChatXml(ChatBaseModel):
    data = CharField(max_length=1023, default='')


class ChatJson(ChatBaseModel):
    data = CharField(max_length=1023, default='')


class ChatText(BaseModel):
    chat_id = BigIntegerField(default=0, help_text='chat id')
    text = CharField(max_length=1023, default='', help_text='纯文本内容')


if __name__ == '__main__':

    c = Chat.get(group_id=1234567, user_id=634493876, message_id=101, type=10)
    c.delete_instance()
