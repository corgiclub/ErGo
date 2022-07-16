FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN apt-get update -o Acquire::http::proxy="http://172.17.0.1:1081/" && \
    apt-get install -y gcc -o Acquire::http::proxy="http://172.17.0.1:1081/"
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-dependencies
CMD ["python", "bot.py"]