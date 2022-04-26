from peewee import BigIntegerField, CharField, SmallIntegerField, BooleanField

from src.models import BaseModel


class Image(BaseModel):
    filename = CharField(max_length=255, default='')
    type_id = SmallIntegerField(default=0)
    suffix = CharField(max_length=4, default='')
    file_existed = BooleanField(default=False)
    p_hash = BigIntegerField(default=0)


class ImageChat(BaseModel):
    # 所有 QQ 聊天中

    image_id = BigIntegerField(default=0)
    qq_hash = CharField(max_length=32, default='')
    qq_count = BigIntegerField(default=0)


class ImageSauce(BaseModel):
    image_id = BigIntegerField(default=0)

    thumbnail = CharField(max_length=1023, default='')
    similarity = CharField(max_length=1023, default='')
    index_id = CharField(max_length=1023, default='')
    index_name = CharField(max_length=1023, default='')
    title = CharField(max_length=1023, default='')
    urls = CharField(max_length=1023, default='')
    author = CharField(max_length=1023, default='')
    raw = CharField(max_length=1023, default='')

    pixiv_id = BigIntegerField(default=0)
    twitter_id = CharField(max_length=1023, default='')

    part = BigIntegerField(default=0)
    year = BigIntegerField(default=0)
    est_time = CharField(max_length=1023, default='')


class ImageTag(BaseModel):
    image_id = BigIntegerField(default=0, help_text='chat id')
    tag_source = SmallIntegerField(default=0)
    tag = CharField(max_length=255, default='')


if __name__ == '__main__':
    print(ImageSauce.get_by_id(2))
