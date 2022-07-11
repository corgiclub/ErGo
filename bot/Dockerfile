FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install bilibili_api==9.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple --ignore-installed

CMD ["python", "bot.py"]