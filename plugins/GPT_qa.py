from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import re
import time

from extensions.cpm_lm.sample import sample


__plugin_name__ = '二狗QA'
__plugin_usage__ = '召唤bot使用模型推理'

bcc = Get.bcc()


def cut_by_symbol(sentence):
    symbols = [',', '，', '.', '。', '《', '》']
    symbol_idx = [sentence.rfind(symbol) for symbol in symbols]
    cut_idx = max(symbol_idx)
    if cut_idx == -1:
        return sentence, ''
    else:
        cutted_segment = sentence[cut_idx:]
        return sentence[:cut_idx], cutted_segment


@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def gpt_qa(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    if message.asDisplay().startswith(('二狗')):
        try:
            msg = message.asDisplay()
            query = msg[2:]
            await app.sendGroupMessage(group, MessageChain.create([
                Plain("稍等 让我想想"),
            ]))

            # 推理
            _begin_time = time.time()
            answer = sample(query, length=100)[0]
            _original_len = len(answer)

            # 截断最后一个符号
            answer, answer_cutted = cut_by_symbol(answer)
            _cutted_len = len(answer)
            _time_taken = int(time.time() - _begin_time)

            # 返回信息
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(answer),
                Plain(10*"-"),
                Plain(f"\n耗时: {_time_taken}s; 句长(截断前/后):{_original_len}/{_cutted_len}; 截断长度:{_original_len - _cutted_len};"),
                Plain(f"\n截断内容: {answer_cutted}")
            ]))
        except ValueError:
            return
