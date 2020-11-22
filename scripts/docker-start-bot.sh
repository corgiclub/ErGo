# 启动docker容器并启动bot
docker container stop ergo-bot-container
docker container rm ergo-bot-container
docker run -v /home/xingyaow/Projects/ErGo:/ErGo -itd --name ergo-bot-container ergo-bot /bin/bash

docker exec ergo-bot-container sh -c "sh /ErGo/scripts/start-bot.sh"
