from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from mirai_core import judge
from mirai_core import Get

import time
import datetime
import requests
from bs4 import BeautifulSoup

__plugin_name__ = '氦'
__plugin_description__ = '呼唤bot'
__plugin_usage__ = '发送"氦"'

bcc = Get.bcc()

# todo 通过 threading 实现每日自动发送

@bcc.receiver(GroupMessage, headless_decoraters=[judge.group_check(__name__)])
async def daily_news(app: GraiaMiraiApplication, group: Group, message: MessageChain, member: Member):
    mes = message.asDisplay()
    if mes in ['今日要闻', '昨日要闻', '早上好二狗', 'おはよう', 'morning~']:

        if mes in ['早上好二狗', 'おはよう', 'morning~']:
            mes = '今日要闻'

        r = requests.get(url='https://mp.sohu.com/profile?xpt=OTk3YTMwMWYtOGNmZS00MzMxLWEzYjktOGE4MjdjZjgwMGI0&_f='
                             'index_pagemp_1&spm=smpc.content.author.2.1606837412545xZ4rTlY')

        if r.status_code != 200:
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(f"网络错误！"),
            ]))
            return

        titles_soup = BeautifulSoup(r.text, 'lxml')
        titles = titles_soup.find_all(class_='feed-title')
        today_ready = get_day() in titles[0].a.get_text()

        if not today_ready and mes == '今日要闻':
            await app.sendGroupMessage(group, MessageChain.create([
                Plain('今日要闻未更新！可输入“昨日要闻”查看昨日要闻。'),
            ]))
            return

        url = ''
        if (today_ready and mes == '今日要闻') or (not today_ready and mes == '昨日要闻'):
            url = 'http:' + titles[0].a['href']
        elif today_ready and mes == '昨日要闻':
            url = 'http:' + titles[1].a['href']

        article = requests.get(url)
        article_soup = BeautifulSoup(article.text, 'lxml')
        article_formated = '\n'.join([p.text[:-1] for p in article_soup.article.find_all('p')[2:-2]])
        await app.sendGroupMessage(group, MessageChain.create([
            Plain(article_formated),
        ]))


def get_day(day='today'):
    time_bjt = datetime.datetime.now() + datetime.timedelta(hours=8)
    # if day == 'yesterday':
    #     time_ls -= datetime.timedelta(days=1)
    time_str = time_bjt.strftime("%m月%d日")
    if time_str[-3] == '0':
        time_str = time_str[:-3] + time_str[-2:]
    return time_str


