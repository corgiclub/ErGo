# 此脚本应在docker容器内运行
cd /ErGo
cd mirai
screen -md -S miraiOK ./miraiOK_linux-amd64
cd ..
screen -md -S bot bash -c 'python3 main.py 2>&1 | tee bot.log'
