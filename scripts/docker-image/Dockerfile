FROM python:3.8

# Change source
RUN rm -f /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list
COPY requirements.txt .

# Install screen
RUN apt-get update
RUN apt-get install screen -y

# Python Packages
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Set PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/ErGo:/ErGo/extensions/cpm_lm"
