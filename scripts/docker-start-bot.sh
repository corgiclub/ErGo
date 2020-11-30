docker container stop ergo-inference-service
docker container rm ergo-inference-service
docker run -v /home/xingyaow/Projects/ErGo:/ErGo -itd --name ergo-inference-service ergo-bot-inference /bin/bash
inference_ip=`docker exec -it ergo-inference-service ip a | grep inet | tail -n1 | awk -F "/" '{print $1}' | awk -F " " '{print $2}'`

# 启动推理
docker exec ergo-inference-service sh -c "sh /ErGo/scripts/start-inference.sh"

# 启动docker容器并启动bot
docker container stop ergo-bot-container
docker container rm ergo-bot-container
docker run --net=container:ergo-inference-service -v /home/xingyaow/Projects/ErGo:/ErGo -itd --name ergo-bot-container ergo-bot /bin/bash
docker exec ergo-bot-container sh -c "sh /ErGo/scripts/start-bot.sh"
