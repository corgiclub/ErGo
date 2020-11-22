FROM python:3.8

# Change source
RUN rm -f /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list

# Install screen
RUN apt-get update
RUN apt-get install screen -y

# Dependency for CPM-LM (Chinese GPT)
RUN pip install sentencepiece jieba regex tensorflow tensorflow-hub -i https://pypi.tuna.tsinghua.edu.cn/simple

# Bot dependency
RUN pip install graia-application-mirai -i https://pypi.tuna.tsinghua.edu.cn/simple

# Set PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/ErGo:/ErGo/extensions/cpm_lm"
