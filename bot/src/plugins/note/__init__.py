import re

from nonebot import on_regex, on_command
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Event, MessageSegment, Bot
from peewee import fn, DoesNotExist

from src.extensions import coolperm, CQ, regex_equal, regex_startswith_key_with_image, get_chat_image, pic_base_path
from src.models.others import Note


note = on_regex(r'^\..+|^。.+', priority=50, block=False)
get_keys = on_command('note', priority=10, block=False)


@note.handle(parameterless=[coolperm('.note')])
async def _(bot: Bot, event: Event):
    # todo 改为记录整条 message

    message = event.get_plaintext().split()
    message = [msg.strip() for msg in message if msg.strip() != '']

    if len(message[0]) <= 1:
        return

    if len(message) == 1:

        # get note in database then send it
        try:
            note_line = Note.select(Note.content).where(Note.note == message[0][1:]).order_by(fn.Rand()).get()
        except DoesNotExist as e:
            logger.warning(e)
        else:
            await note.finish(MessageSegment.text(note_line.content))
    else:
        # save note in database
        key = message[0][1:]
        content = ' '.join(message[1:])
        if len(key) > 32:
            await note.finish(MessageSegment.text(text='key 长度不能超过32'))
        if len(content) > 255:
            await note.finish(MessageSegment.text(text='内容长度不能超过255'))
        _, created = Note.get_or_create(note=key, content=content)
        if created:
            await note.finish(MessageSegment.text(text='已记录'))
        else:
            await note.finish(MessageSegment.text(text='已存在'))


@get_keys.handle(parameterless=[coolperm('.list')])
async def _(bot: Bot, event: Event):
    message = '目前存储的 key (最近20条):'
    for key in Note.select(Note.note).order_by(Note.add_time.desc()).limit(20):
        message += f"\n{key.note}"
    await get_keys.finish(MessageSegment.text(text=message))
