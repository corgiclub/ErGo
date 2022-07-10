FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["glances", "-w", "--disable-webui"]