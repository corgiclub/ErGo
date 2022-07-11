FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-dependencies
CMD ["python", "bot.py"]