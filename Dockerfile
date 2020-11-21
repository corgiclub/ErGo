FROM python:3.6

WORKDIR .

# Dependency for CPM-LM (Chinese GPT)
RUN pip install sentencepiece jieba regex tensorflow tensorflow-hub -i https://pypi.tuna.tsinghua.edu.cn/simple

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

