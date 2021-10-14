import datetime
import os

from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message

from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime
from alchemical import Alchemical

db = Alchemical('sqlite:///ergo.sqlite')


class Note(db.Model):
    id = Column(Integer, primary_key=True)
    qq = Column(BigInteger)
    msg = Column(Text, nullable=False)
    add_time = Column(DateTime, default=datetime.datetime.now)


db.create_all()

note = on_command('note', priority=10, block=False)
note_all = on_command('noteall', priority=10, block=False)
note_my = on_command('notemy', priority=10, block=False)


@note.handle()
async def _(bot: Bot, event: Event, state: T_State):
    from_msg = str(event.get_message())
    if not from_msg:
        await note.send('请按照「/note 内容」来存东西')
        return
    sender = int(event.get_user_id())
    with db.begin() as session:
        session.add(Note(qq=sender, msg=from_msg))
    to_msg = Message([
        {
            'type': 'at',
            'data': {
                'qq': sender
            }
        },
        {
            'type': 'text',
            'data': {
                'text': f'已保存 {from_msg}'
            }
        }
    ])
    await note.send(to_msg)


@note_my.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sender = int(event.get_user_id())
    with db.Session() as session:
        notes = session.scalars(Note.select().where(Note.qq == sender)).all()
        await note_my.send('\n'.join([f'{nt.msg} {nt.add_time}' for nt in notes]))
