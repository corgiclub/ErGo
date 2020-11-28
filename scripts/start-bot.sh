# 此脚本应在docker容器内运行
cd /ErGo
mkdir logs
# 启动miral
cd mirai
screen -md -S miraiOK ./miraiOK_linux-amd64
cd /ErGo
# 启动推理服务器
cd extensions/cpm_lm
screen -md -S cpmlm-inference bash -c 'python3 wsgi.py 2>&1 | tee /ErGo/logs/cpm_lm_inference.log'
cd /ErGo
sleep 3
# 启动bot
screen -md -S bot bash -c 'python3 main.py 2>&1 | tee logs/bot.log'
