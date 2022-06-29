from peewee import BigIntegerField, CharField, SmallIntegerField, BooleanField, FloatField, DateTimeField, IntegerField

from src.models import BaseModel


class Image(BaseModel):
    url = CharField(max_length=255, default='')
    filename = CharField(max_length=255, default='')
    type_id = SmallIntegerField(default=0)
    suffix = CharField(max_length=4, default='')
    file_existed = BooleanField(default=False)
    p_hash = BigIntegerField(default=0)
    fix_count = SmallIntegerField(default=0)


class ImageChat(BaseModel):
    # 所有 QQ 聊天中

    image_id = BigIntegerField(default=0)
    qq_hash = CharField(max_length=32, default='')
    qq_count = BigIntegerField(default=0)


class ImageSauce(BaseModel):
    image_id = BigIntegerField(default=0)

    thumbnail = CharField(max_length=255, default='')
    similarity = FloatField(default=0)
    index_id = BigIntegerField(default='')
    index_name = CharField(max_length=255, default='')
    title = CharField(max_length=255, default='')
    url = CharField(max_length=255, default='')
    author = CharField(max_length=50, default='')

    pixiv_id = BigIntegerField(default=0)
    member_id = BigIntegerField(default=0)


class ImageTag(BaseModel):
    image_id = BigIntegerField(default=0, help_text='image id')
    tag_source = SmallIntegerField(default=0)
    tag = CharField(max_length=255, default='')


class ImageGallery(BaseModel):
    image_id = BigIntegerField(default=0, help_text='image id')
    theme = CharField(max_length=32, default='')


class ImagePixiv(BaseModel):
    image_id = BigIntegerField(default=0, help_text='image id')

    pixiv_id = BigIntegerField(default=0)
    author_id = IntegerField(default=0)
    title = CharField(max_length=255, default='')
    bookmarks = IntegerField(default=0)
    view = IntegerField(default=0)
    illust_type = CharField(max_length=32, default='')
    page_count = SmallIntegerField(default=0)
    page = SmallIntegerField(default=0)
    sanity_level = SmallIntegerField(default=0)
    x_restrict = BooleanField(default=False)
    image_url = CharField(max_length=255, default='')
    create_date = DateTimeField()



if __name__ == '__main__':
    print(ImageSauce.get_by_id(2))
