docker container stop ergo-inference-service
docker container rm ergo-inference-service
docker run \
-p 6666:6666 \
-v /home/xingyaow/Projects/ErGo:/ErGo -itd --name ergo-inference-service ergo-bot-inference /bin/bash

# 启动推理
docker exec ergo-inference-service sh -c "sh /ErGo/scripts/start-inference.sh"

