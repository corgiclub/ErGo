# 启动推理服务器
# 此脚本应在docker容器内运行
cd /ErGo
mkdir logs
# 启动推理
cd extensions/cpm_lm
screen -md -S cpmlm-inference bash -c 'python3 wsgi.py 2>&1 | tee /ErGo/logs/cpm_lm_inference.log'
cd /ErGo
