FROM python:3.8

# Dependency for CPM-LM (Chinese GPT)
RUN pip install sentencepiece jieba regex tensorflow tensorflow-hub -i https://pypi.tuna.tsinghua.edu.cn/simple

# Bot dependency
RUN pip install graia-application-mirai -i https://pypi.tuna.tsinghua.edu.cn/simple

